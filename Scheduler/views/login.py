from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from Scheduler.models.Restaurant import Restaurant


class Login(View):

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

                # Get Restaurant
                restaurant = user.restaurant
                request.session['restaurant_id'] = restaurant.restaurant_id

                # Get and set session restaurant name
                restaurant_name = restaurant.restaurant_name
                request.session['restaurant_name'] = restaurant_name
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
