from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

from Scheduler.models import User, Restaurant


class AllUsers(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        current_user = request.user
        allUsers = User.objects.all()
        form = AuthenticationForm
        message = request.session.get("message")
        request.session.delete("message")
        if message == None:
            message = ""

        context = {
            'restaurant_name': restaurant_name,
            'userList': allUsers,
            'message': message,
            'current_user': current_user,
            'current_user_role': current_user.role,
        }
        return render(request, 'Scheduler/allUser.html', context)
