from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import User, Restaurant
from django.db import IntegrityError


class AccountCreation(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'restaurant_name': restaurant_name
        }
        return render(request, "Scheduler/accountcreation.html", context)

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zipcode"]
        role = request.POST["role"]
        password = request.POST["password"]
        restaurant=Restaurant.objects.get(restaurant_name=request.session.get('restaurant_name'))
        status = ""

        try:
            user = User(role=role,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password,
                        address=address,
                        city=city,
                        restaurant=restaurant,
                        state=state,
                        zip_code=zip_code,
                        username=email)
            user.save()
            status = "Successfully created the user."
        except IntegrityError:
            status = "Users with duplicate emails are not allowed."
        except Exception as e:
            status = e
        return render(request, "Scheduler/accountcreation.html", {'status': status})