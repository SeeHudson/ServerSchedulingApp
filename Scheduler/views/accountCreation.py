from django.shortcuts import render, redirect
from django.views import View


class AccountCreation(View):
    def get(self, request):
        return render(request, "Scheduler/accountcreation.html")
