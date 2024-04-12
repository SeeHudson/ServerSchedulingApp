from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import Employee, Shift, EmployeeShift
from django.db import IntegrityError


class AddShifts(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        current_user = request.user
        context={
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'employees': Employee.objects.all(),
            'restaurant_name': restaurant_name,
            'current_user_role': current_user.role,
        }
        return render(request, "Scheduler/add_shifts.html", context)

    def post(self, request):
        restaurant_name = request.session.get('restaurant_name')

        selected_employees = request.POST.getlist('employees')
        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        status = ""
        for day in days:
            shift_types = request.POST.getlist(f"{day}Availability")
            for shift_type in shift_types:
                try:
                    shift, created = Shift.objects.get_or_create(day=day, shift_type=shift_type)
                    for employee_id in selected_employees:
                        employee = Employee.objects.get(pk=employee_id)
                        if EmployeeShift.objects.filter(user=employee, shift=shift).exists():
                            status = f"Shift already exists for {employee.user.get_full_name()} on {day} ({shift_type})."
                        else:
                            employeeShift = EmployeeShift.objects.create(user=employee, shift=shift)
                            employeeShift.save()
                            status = "Successfully created the shift."
                except Exception as e:
                    status = e
        context = {
            'days': days,
            'employees': Employee.objects.all(),
            'restaurant_name': restaurant_name,
            'status': status
        }

        return render(request, "Scheduler/add_shifts.html", context)