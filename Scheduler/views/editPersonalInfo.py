from django.shortcuts import render, redirect
from django.views import View


class EditPersonalInfo(View):
    def get(self, request):
        current_user = request.user
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'email': current_user.email,
            'restaurant_name': restaurant_name
        }
        return render(request, "Scheduler/editPersonalInfo.html", context)