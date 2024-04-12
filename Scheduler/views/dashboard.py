from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models.Shift import Shift
from Scheduler.models.User import User
from Scheduler.models.Restaurant import Restaurant
from Scheduler.models.Employee import Employee
from Scheduler.models.Manager import Manager


class Dashboard(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        current_user = request.user

        employees_shifts = None

        if current_user.role == 'EMPLOYEE':
            employee = Employee.objects.get(user=current_user)
            employees_shifts = employee.get_all_shifts_for_employee()

        if current_user.role == 'MANAGER':
            manager = Manager.objects.get(user=current_user)
            restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)
            employees_shifts = restaurant.get_all_shifts()
            return render(request, "Scheduler/dashboard.html", {'restaurant_name': restaurant_name, 'employees_shifts': employees_shifts, 'current_user': current_user})

        if employees_shifts is not None:
            monday_shifts = employees_shifts.filter(day='Mo')
            tuesday_shifts = employees_shifts.filter(day='Tu')
            wednesday_shifts = employees_shifts.filter(day='We')
            thursday_shifts = employees_shifts.filter(day='Th')
            friday_shifts = employees_shifts.filter(day='Fr')
            saturday_shifts = employees_shifts.filter(day='Sa')
            sunday_shifts = employees_shifts.filter(day='Su')

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        shift_types = ["Open", "Mid", "Close"]
        shifts_by_day = []
        for day in days:
            shifts = Shift.objects.filter(day__in=[day[:2], day])
            shifts_by_day.append({"day": day, "shifts": shifts})

        context = {
            'restaurant_name': restaurant_name,
            'employees_shifts': employees_shifts,
            'monday_shifts': monday_shifts,
            'tuesday_shifts': tuesday_shifts,
            'wednesday_shifts': wednesday_shifts,
            'thursday_shifts': thursday_shifts,
            'friday_shifts': friday_shifts,
            'saturday_shifts': saturday_shifts,
            'sunday_shifts': sunday_shifts,
            'current_user': current_user,
            'current_user_role': current_user.role,
            "shifts_by_day": shifts_by_day,
            "shift_types": shift_types,
        }
        return render(request, "Scheduler/dashboard.html", context)
