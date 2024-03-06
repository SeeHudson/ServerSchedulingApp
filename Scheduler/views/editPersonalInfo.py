from django.shortcuts import render, redirect
from django.views import View


class EditPersonalInfo(View):
    def get(self, request):
        return render(request, "Scheduler/editPersonalInfo.html")