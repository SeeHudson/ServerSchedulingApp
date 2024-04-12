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

        }
        return render(request, "Scheduler/editPersonalInfo.html", context)

    def post(self, request):
        current_user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone_number"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zipcode"]
        status = ""

        try:
            if (first_name != ""):
                current_user.set_first_name(first_name)

            if (last_name != ""):
                current_user.set_last_name(last_name)

            if (phone != ""):
                current_user.set_phone_number(phone)

            if (address != ""):
                current_user.set_address(address)

            if (city != ""):
                current_user.set_city(city)

            if (state != ""):
                current_user.set_state(state)

            if (zip_code != ""):
                current_user.set_zip_code(zip_code)

            status = "Successfully updated this user."
        except IntegrityError:
            status = "Users with duplicate emails are not allowed."
        except Exception as e:
            status = e
        return render(request, "Scheduler/editPersonalInfo.html", {'status': status})
