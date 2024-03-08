from django.shortcuts import render, redirect
from django.views import View


class Account(View):
    def get(self, request):
        return render(request, "Scheduler/account.html")