from django.shortcuts import render, redirect
from django.views import View


class TimeOff(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'restaurant_name': restaurant_name
        }
        return render(request, "Scheduler/timeOff.html",context)