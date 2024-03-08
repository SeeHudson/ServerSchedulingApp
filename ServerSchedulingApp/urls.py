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
from Scheduler.views import Account, Dashboard, EditPersonalInfo, Login
from Scheduler.views.creation import Creation
from Scheduler.views.updateAvailablilty import UpdateAvailability


urlpatterns = [
    # Might need to be removed
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('display_all_shifts/', Display_All_Shifts.as_view(), name='display_all_shifts'),
    path('account/editPersonalInfo/', EditPersonalInfo.as_view(), name='editPersonalInfo'),
    path('account/', Account.as_view(), name='account'),
    path('serverscore/', ServerScore.as_view(), name='serverscore'),
    path('dashboard/account/editPersonalInfo/', EditPersonalInfo.as_view(), name='editPersonalInfo'),
    path('dashboard/account/accountcreation/', Creation.as_view(), name='creation'),
    path('dashboard/account/updateavailability/', UpdateAvailability.as_view(), name='updateAvailability'),
    path('dashboard/account/', Account.as_view(), name='account')
]
