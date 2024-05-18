from Scheduler.models.Availability import Availability
from Scheduler.models.Employee import Employee
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import transaction

class UpdateAvailability(View):
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_shifts = {day: ['open', 'mid', 'close'] for day in day_order}
    day_map = {
        'Mo': 'Monday',
        'Tu': 'Tuesday',
        'We': 'Wednesday',
        'Th': 'Thursday',
        'Fr': 'Friday',
        'Sa': 'Saturday',
        'Su': 'Sunday',
    }
    reverse_day_map = {v: k for k, v in day_map.items()}  # Reverse mapping

    @method_decorator(login_required)
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        employee = Employee.objects.get(user=request.user)
        availabilities = Availability.objects.filter(employee=employee).order_by('day')
        sorted_availabilities = sorted(availabilities, key=lambda x: self.day_order.index(self.day_map[x.day]))
        current_availabilities = {
            self.day_map[availability.day]: {availability.shift_type: True}
            for availability in sorted_availabilities
        }
        context = {
            'days': self.day_shifts,
            'current_availabilities': current_availabilities,
            'restaurant_name': restaurant_name,
        }
        return render(request, 'Scheduler/updateavailability.html', context)

    @method_decorator(login_required)
    def post(self, request):
        employee = Employee.objects.get(user=request.user)
        with transaction.atomic():
            for day in self.day_order:
                abbreviated_day = self.reverse_day_map[day]  # Get abbreviated form
                shifts = self.day_shifts[day]
                for shift in shifts:
                    checkbox_name = f'{day}_{shift}'
                    if request.POST.get(checkbox_name):
                        Availability.objects.update_or_create(
                            employee=employee, day=abbreviated_day, shift_type=shift,
                            defaults={'employee': employee, 'day': abbreviated_day, 'shift_type': shift}
                        )
                    else:
                        Availability.objects.filter(employee=employee, day=abbreviated_day, shift_type=shift).delete()
        return redirect('account')
