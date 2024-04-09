from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

from Scheduler.models import Restaurant


class AllUsers(View):
    def get(self, request):
        allUsers = Restaurant.get_all_employees()
        form = AuthenticationForm
        message = request.session.get("message")
        request.session.delete("message")
        if message == None:
            message = ""
        return render(request, 'Scheduler/allUser.html', {'userList': allUsers, 'message': message})
