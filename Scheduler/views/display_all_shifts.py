from django.shortcuts import render
from Scheduler.models.Shift import Shift
from django.views import View


class Display_All_Shifts(View):
    def get(self, request):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        shift_types = ["Open", "Mid", "Close"]

        shifts_by_day = []
        for day in days:
            shifts = Shift.objects.filter(day__in=[day[:2], day])
            shifts_by_day.append({"day": day, "shifts": shifts})

        context = {
            "shifts_by_day": shifts_by_day,
            "shift_types": shift_types,
        }
        return render(request, "Scheduler/display_all_shifts.html", context)