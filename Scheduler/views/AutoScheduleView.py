# scheduler/views.py
from django.views import View
from django.shortcuts import redirect, render
import random
from django.db import transaction
from Scheduler.models import Employee, Shift, EmployeeShift, Availability

class AutoScheduleView(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        current_user = request.user

        employees = Employee.objects.all()
        shifts = Shift.objects.all()

        assigned_employees = {shift.pk: [es.user.pk for es in EmployeeShift.objects.filter(shift=shift)] for shift in shifts}

        context = {
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'shift_types': ["Open", "Mid", "Close"],
            'employees': employees,
            'restaurant_name': restaurant_name,
            'current_user_role': current_user.role,
            'assigned_employees': assigned_employees,
        }
        return render(request, "Scheduler/auto_schedule.html", context)

    def post(self, request):
        restaurant_name = request.session.get('restaurant_name')
        employees = list(Employee.objects.all())
        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        shift_types = ["Open", "Mid", "Close"]
        status = ""

        try:
            with transaction.atomic():
                # Clear all existing shifts
                EmployeeShift.objects.all().delete()

                for day in days:
                    for shift_type in shift_types:
                        shift, created = Shift.objects.get_or_create(day=day, shift_type=shift_type)
                        random.shuffle(employees)  # Shuffle employees for random assignment

                        assigned_count = 0
                        for employee in employees:
                            if Availability.objects.filter(employee=employee, day=day, shift_type=shift_type).exists():
                                if not EmployeeShift.objects.filter(user=employee, shift=shift).exists():
                                    EmployeeShift.objects.create(user=employee, shift=shift)
                                    assigned_count += 1
                                    if assigned_count >= 2:
                                        break

            status = "Successfully generated the schedule."
        except Exception as e:
            status = str(e)

        context = {
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'shift_types': ["Open", "Mid", "Close"],
            'employees': Employee.objects.all(),
            'restaurant_name': restaurant_name,
            'status': status
        }

        return render(request, "Scheduler/add_shifts.html", context)
