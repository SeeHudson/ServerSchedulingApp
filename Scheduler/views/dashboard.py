from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models.Shift import Shift


class Dashboard(View):
    def get(self, request):
        friday_shifts = Shift.objects.filter(day='Fr')
        context = {
            'friday_shifts': friday_shifts
        }
        return render(request, "Scheduler/dashboard.html", context)
