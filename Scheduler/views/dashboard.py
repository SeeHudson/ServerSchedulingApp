from django.shortcuts import render
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

        shifts_by_day = {}
        shift_types = ["Open", "Mid", "Close"]

        if current_user.role == 'EMPLOYEE':
            employee = Employee.objects.get(user=current_user)
            employees_shifts = employee.get_all_shifts_for_employee()
        elif current_user.role == 'MANAGER':
            manager = Manager.objects.get(user=current_user)
            restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)
            employees_shifts = restaurant.get_all_shifts()
        else:
            employees_shifts = Shift.objects.none()

        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            day_shifts = employees_shifts.filter(day__in=[day[:2], day])
            shifts_by_day[day] = day_shifts

        context = {
            'restaurant_name': restaurant_name,
            'shifts_by_day': shifts_by_day,
            'shift_types': shift_types,
            'current_user': current_user,
        }
        return render(request, "Scheduler/dashboard.html", context)
