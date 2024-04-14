# views.py - Revised to fix availability display in Account page

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from Scheduler.models import Employee, Availability


class Account(LoginRequiredMixin, View):
    def get(self, request):
        current_user = request.user
        if current_user.role == 'MANAGER':
            context = {
                'restaurant_name': request.session.get('restaurant_name'),
                'current_user_role': current_user.role,
            }
            return render(request, "Scheduler/account.html", context)

        employee = Employee.objects.get(user=current_user)
        # Fetching the availability
        availabilities = Availability.objects.filter(employee=employee)
        availability_dict = {day: [] for day in
                             ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']}
        for availability in availabilities:
            day_name = availability.get_day_display()
            availability_dict[day_name].append(availability.get_shift_type_display())

        # Formatting the availability for display
        availability_display = []
        for day, shifts in availability_dict.items():
            formatted_shifts = ', '.join(shifts) if shifts else 'Not Available'
            availability_display.append((day, formatted_shifts))

        context = {
            'restaurant_name': request.session.get('restaurant_name'),
            'current_user_role': current_user.role,
            'availability_display': availability_display,
        }
        return render(request, "Scheduler/account.html", context)