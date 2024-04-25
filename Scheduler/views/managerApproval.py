from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import User, TimeOff
from django.contrib.auth.forms import AuthenticationForm


class ManagerApproval(View):
    def get(self, request):
        allTimeOff = TimeOff.objects.all().filter(approved=False)
        form = AuthenticationForm
        restaurant_name = request.session.get('restaurant_name')
        message = request.session.get("message")
        request.session.delete("message")
        if message == None:
            message = ""
        context={
            'allTimeOff': allTimeOff,
            'message': message,
            'restaurant_name': restaurant_name,
            'status': "Pending"
        }
        return render(request, "Scheduler/managerApproval.html", context)

    def post(self, request):
        name = request.POST["username"]
        user = User.objects.get(username=name)
        start_date_str = request.POST["start_date"]
        end_date_str = request.POST["end_date"]
        reason = request.POST["reason"]

        start_date = datetime.strptime(start_date_str, "%B %d, %Y")
        start_date_formatted = start_date.strftime("%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%B %d, %Y")
        end_date_formatted = end_date.strftime("%Y-%m-%d")

        timeoffpost = TimeOff.objects.get(user=user,
                                          start_date=start_date_formatted,
                                          end_date=end_date_formatted,
                                          reason=reason,
                                          approved=False)
        status = "Pending"
        if request.POST.get('options') == 'Approve':
            timeoffpost.approved = True
            timeoffpost.save()
            status = "Approved"
        elif request.POST.get('options') == 'Decline':
            timeoffpost.delete()
            status = "Declined"

        return render(request, "Scheduler/managerApproval.html", {'status': status})