from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

from Scheduler.models import User


class AllUsers(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        allUsers = User.objects.all()
        form = AuthenticationForm
        message = request.session.get("message")
        request.session.delete("message")
        if message == None:
            message = ""

        context = {
            'userList': allUsers,
            'message': message,
            'restaurant_name': restaurant_name
        }
        return render(request, 'Scheduler/allUser.html', context)