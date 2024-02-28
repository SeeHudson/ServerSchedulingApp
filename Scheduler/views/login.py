from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm


class Login(View):
    # def index(request):
    #     if not request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('login'))
    #     if request.method == 'GET':
    #         return render(request, 'Scheduler/login.html')  # To-Do: Fix
    #     return HttpResponseRedirect(reverse(request.POST['pageURL']))
    def get(self, request):
        form = AuthenticationForm
        return render(request, 'Scheduler/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                # Return an 'invalid login' error message.
                return render(request, 'Scheduler/login.html',
                              {'form': form, 'error_message': 'Invalid username or password.', 'hide_navbar': True})
        else:
            return render(request, 'Scheduler/login.html',
                          {'form': form, 'error_message': 'Invalid username or password.', 'hide_navbar': True})

    def logout_view(request):
        logout(request)
        return render(request, "Scheduler/dashboard.html", {
            'message': "Logged out"
        })
