from django.shortcuts import render, redirect
from django.views import View


class TimeOff(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        current_user = request.user
        context = {
            'restaurant_name': restaurant_name,
            "current_user": current_user,
            'current_user_role': current_user.role,
        }
        return render(request, "Scheduler/timeOff.html",context)