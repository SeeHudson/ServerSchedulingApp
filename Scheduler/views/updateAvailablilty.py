from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models.Availability import Availability
from Scheduler.models.Employee import Employee
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class UpdateAvailability(View):
    def get(self, request):
        days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        return render(request, 'Scheduler/updateavailability.html', {'days': days})

    def post(self, request):
        employee = Employee.objects.get(user=request.user)
        for day in ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']:
            for shift_type in ['open', 'mid', 'close']:
                # Check if checkbox for the day and shift type is on
                if request.POST.get(f'{day}{shift_type}') == 'on':
                    Availability.objects.update_or_create(
                        employee=employee,
                        day=day,
                        shift_type=shift_type,
                        defaults={'employee': employee, 'day': day, 'shift_type': shift_type}
                    )
                else:
                    # If checkbox is not checked, delete the availability if it exists
                    Availability.objects.filter(employee=employee, day=day, shift_type=shift_type).delete()

        return redirect('dashboard')
