from django.shortcuts import render, redirect
from django.views import View


class Dashboard(View):
    def get(self, request):
        return render(request, "Scheduler/dashboard.html")
