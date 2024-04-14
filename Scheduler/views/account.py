# views.py - Revised to fix availability display in Account page
from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import Employee, Availability
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Account(View):
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        employee = Employee.objects.get(user=user)
        availabilities = Availability.objects.filter(employee=employee).order_by('day')

        availability_dict = {day: None for day in self.day_order}
        for availability in availabilities:
            day_name = availability.get_day_display()
            availability_dict[day_name] = availability.get_shift_type_display()

        availability_display = [(day, availability_dict[day]) for day in self.day_order if availability_dict[day]]

        context = {
            'user': user,
            'availability_display': availability_display,
            'restaurant_name': "Your Restaurant Name",
        }
        return render(request, 'Scheduler/account.html', context)