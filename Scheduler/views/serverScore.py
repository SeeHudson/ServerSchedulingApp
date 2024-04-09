from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

import Scheduler
from Scheduler.models import Employee, User

class ServerScore(View):
    def get(self, request):

        if request.method == 'GET':
            return render(request, "Scheduler/serverscore.html")


def post(self, request):
    score1 = request.POST['score2']
    score2 = request.POST['score3']
    score3 = request.POST['score4']
    score4 = request.POST['score5']
    score5 = request.POST['newScore']
    average_score = ((score1 + score2 + score3 + score4 + score5 ) / 5)

    return render(request, "Scheduler/serverscore.html")
                  # {'employee': thisUser, 'isAdmin': isAdmin, 'isUser': isUser, 'message': message})
