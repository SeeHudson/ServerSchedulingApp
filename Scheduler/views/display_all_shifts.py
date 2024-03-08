from django.shortcuts import render
from Scheduler.models.Shift import Shift
from django.views import View


class Display_All_Shifts(View):
    def get(self, request):
        shifts = Shift.objects.all().order_by('day', 'startTime')  # Ordering by day and start time for convenience
        monday_shifts = Shift.objects.filter(day='Mo')
        tuesday_shifts = Shift.objects.filter(day='Tu')
        wednesday_shifts = Shift.objects.filter(day='We')
        thursday_shifts = Shift.objects.filter(day='Th')
        friday_shifts = Shift.objects.filter(day='Fr')
        saturday_shifts = Shift.objects.filter(day='Sa')
        sunday_shifts = Shift.objects.filter(day='Su')

        context = {
            'shifts': shifts,
            'monday_shifts': monday_shifts,
            'tuesday_shifts': tuesday_shifts,
            'wednesday_shifts': wednesday_shifts,
            'thursday_shifts': thursday_shifts,
            'friday_shifts': friday_shifts,
            'saturday_shifts': saturday_shifts,
            'sunday_shifts': sunday_shifts,
        }
        return render(request, 'Scheduler/display_all_shifts.html', context)