# views.py

from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import Employee, Shift, EmployeeShift


class AddShifts(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        current_user = request.user

        # Fetch all employees and shifts
        employees = Employee.objects.all()
        shifts = Shift.objects.all()

        # Create a dictionary to track assigned employees for each shift
        assigned_employees = {shift.pk: [es.user.pk for es in EmployeeShift.objects.filter(shift=shift)] for shift in
                              shifts}

        context = {
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'shift_types': ["Open", "Mid", "Close"],
            'employees': employees,
            'restaurant_name': restaurant_name,
            'current_user_role': current_user.role,
            'assigned_employees': assigned_employees,
        }
        return render(request, "Scheduler/add_shifts.html", context)

    def post(self, request):
        restaurant_name = request.session.get('restaurant_name')
        selected_employees = request.POST.getlist('employees')
        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        status = ""

        for day in days:
            shift_types = request.POST.getlist(f"{day}Availability")

            # Clear existing shifts for the current day for selected employees
            shifts_to_clear = Shift.objects.filter(day=day)
            EmployeeShift.objects.filter(shift__in=shifts_to_clear, user__pk__in=selected_employees).delete()

            for shift_type in shift_types:
                try:
                    shift, created = Shift.objects.get_or_create(day=day, shift_type=shift_type)
                    for employee_pk in selected_employees:
                        employee = Employee.objects.get(pk=employee_pk)
                        if not EmployeeShift.objects.filter(user=employee, shift=shift).exists():
                            employeeShift = EmployeeShift.objects.create(user=employee, shift=shift)
                            employeeShift.save()
                            status = "Successfully created the shift."
                except Exception as e:
                    status = e

        context = {
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'shift_types': ["Open", "Mid", "Close"],
            'employees': Employee.objects.all(),
            'restaurant_name': restaurant_name,
            'status': status
        }

        return render(request, "Scheduler/add_shifts.html", context)
