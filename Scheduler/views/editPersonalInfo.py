from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import User, Restaurant
from django.db import IntegrityError

class EditPersonalInfo(View):
    def get(self, request):
        current_user = request.user
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'restaurant_name': restaurant_name,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'email': current_user.email,
            "current_user": current_user,
            'current_user_role': current_user.role,
        }
        return render(request, "Scheduler/editPersonalInfo.html", context)

    def post(self, request):
        current_user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone_number"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zipcode"]
        status = ""

        try:
            if first_name != "":
                current_user.first_name = first_name

            if last_name != "":
                current_user.last_name = last_name

            if email != "":
                current_user.email = email

            if phone != "":
                current_user.phone_number = phone

            if address != "":
                current_user.address = address

            if city != "":
                current_user.city = city

            if state != "":
                current_user.state = state

            if zip_code != "":
                current_user.zip_code = zip_code

            current_user.save()
            status = "Successfully updated this user."
        except IntegrityError:
            status = "Users with duplicate emails are not allowed."
        except Exception as e:
            status = str(e)

        context = {
            'restaurant_name': request.session.get('restaurant_name'),
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'email': current_user.email,
            'phone_number': current_user.phone_number,
            'address': current_user.address,
            'city': current_user.city,
            'state': current_user.state,
            'zipcode': current_user.zip_code,
            "current_user": current_user,
            'current_user_role': current_user.role,
            'status': status
        }
        return render(request, "Scheduler/editPersonalInfo.html", context)
