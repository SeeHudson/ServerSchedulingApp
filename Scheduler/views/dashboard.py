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

        if employees_shifts is not None:
            monday_shifts = employees_shifts.filter(day='Mo')
            tuesday_shifts = employees_shifts.filter(day='Tu')
            wednesday_shifts = employees_shifts.filter(day='We')
            thursday_shifts = employees_shifts.filter(day='Th')
            friday_shifts = employees_shifts.filter(day='Fr')
            saturday_shifts = employees_shifts.filter(day='Sa')
            sunday_shifts = employees_shifts.filter(day='Su')

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
        }
        return render(request, "Scheduler/dashboard.html", context)
