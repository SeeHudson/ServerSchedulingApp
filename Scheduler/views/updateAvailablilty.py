from django.shortcuts import render, redirect
from django.views import View
class UpdateAvailability(View):
    context = {
        'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    }
    def get(self, request):
        return render(request, 'Scheduler/updateavailability.html',
                      {'days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]})
