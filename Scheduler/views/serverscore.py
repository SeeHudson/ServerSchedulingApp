from django.shortcuts import render, redirect
from django.views import View


class ServerScore(View):
    def get(self, request):
        return render(request, "Scheduler/serverscore.html")