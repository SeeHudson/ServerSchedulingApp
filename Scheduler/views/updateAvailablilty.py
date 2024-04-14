from Scheduler.models.Availability import Availability
from Scheduler.models.Employee import Employee
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import transaction
from django.contrib import messages

class UpdateAvailability(View):
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_shifts = {day: ['open', 'mid', 'close'] for day in day_order}

    @method_decorator(login_required)
    def get(self, request):
        employee = Employee.objects.get(user=request.user)
        availabilities = Availability.objects.filter(employee=employee).order_by('day')
        sorted_availabilities = sorted(availabilities, key=lambda x: self.day_order.index(x.day))
        current_availabilities = {
            availability.day + availability.shift_type: True
            for availability in sorted_availabilities
        }
        context = {
            'days': self.day_shifts,
            'current_availabilities': current_availabilities,
        }
        return render(request, 'Scheduler/updateavailability.html', context)

    @method_decorator(login_required)
    def post(self, request):
        employee = Employee.objects.get(user=request.user)
        with transaction.atomic():
            for day in self.day_order:
                shifts = self.day_shifts[day]
                for shift in shifts:
                    checkbox_name = f'{day}{shift}'
                    if request.POST.get(checkbox_name) == 'on':
                        Availability.objects.update_or_create(
                            employee=employee, day=day, shift_type=shift,
                            defaults={'employee': employee, 'day': day, 'shift_type': shift}
                        )
                    else:
                        Availability.objects.filter(employee=employee, day=day, shift_type=shift).delete()
            messages.success(request, "Your availability has been updated successfully.")
        return redirect('dashboard')