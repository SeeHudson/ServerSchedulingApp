from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models.Employee import Employee


class AddShifts(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        context={
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'employees': Employee.objects.all(),
            'restaurant_name': restaurant_name
        }
        return render(request, "Scheduler/add_shifts.html", context)

    def post(self, request):
        restaurant_name = request.session.get('restaurant_name')
        context={
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'employees': Employee.objects.all(),
            'restaurant_name': restaurant_name
        }
        return render(request, "Scheduler/add_shifts.html", context)