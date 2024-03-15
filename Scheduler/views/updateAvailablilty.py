from django.shortcuts import render, redirect
from django.views import View
class UpdateAvailability(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'restaurant_name': restaurant_name
        }
        return render(request, 'Scheduler/updateavailability.html', context)

    def post(self, request):
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'restaurant_name': restaurant_name
        }
        return render(request, 'Scheduler/updateavailability.html', context)
