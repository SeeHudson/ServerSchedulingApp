from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from Scheduler.models import TimeOff as TimeOffModel


class TimeOff(View):
    def get(self, request):
        restaurant_name = request.session.get('restaurant_name')
        context = {
            'restaurant_name': restaurant_name
        }
        return render(request, "Scheduler/timeOff.html", context)

    def post(self, request):
        employee = request.user
        start_date_str = request.POST["start_date"]
        end_date_str = request.POST["end_date"]
        reason = request.POST["time_off_reason"]
        status = ""

        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        if start_date > end_date:
            status = "Invalid form response"
            return render(request, "Scheduler/timeOff.html", {'status': status})

        timeoffrequest = TimeOffModel(user=employee,
                                 start_date=start_date,
                                 end_date=end_date,
                                 reason=reason,
                                 approved=False)
        timeoffrequest.save()

        status = "Successful time off submission"

        return render(request, "Scheduler/timeOff.html", {'status': status})