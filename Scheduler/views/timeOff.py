from django.shortcuts import render, redirect
from django.views import View


class TimeOff(View):
    def get(self, request):
        return render(request, "Scheduler/timeOff.html")