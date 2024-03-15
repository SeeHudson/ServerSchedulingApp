"""
URL configuration for ServerSchedulingApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from Scheduler import views
from Scheduler.views import *
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect to the login page
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('dashboard/dashboard', Dashboard.as_view(), name="dashboard"),
    path('dashboard/allUsers/', AllUsers.as_view(), name="viewAllUsers"),
    path('serverScore/', ServerScore.as_view(), name="serverScore"),
    path('dashboard/account/editPersonalInfo/', EditPersonalInfo.as_view(), name='editPersonalInfo'),
    path('dashboard/account/', Account.as_view(), name='account'),
    path('dashboard/account/updateAvailability/', UpdateAvailability.as_view(), name='updateAvailability'),
    path('dashboard/account/timeOff/', TimeOff.as_view(), name='timeOff')

]
