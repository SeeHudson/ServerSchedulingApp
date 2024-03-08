from django.db import models
from django.utils.translation import gettext_lazy as _
from .Employee import Employee


class Shift(models.Model):
    Day_of_Week = (
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
    )

    day = models.CharField(max_length=2, choices=Day_of_Week)
    # Maybe use TimeInput widget in forms
    startTime = models.TimeField(_('Start Time'))
    endTime = models.TimeField(_('End Time'))
    # Many-to-Many relationship with Employee
    employees = models.ManyToManyField(Employee, through='EmployeeShift', related_name='shifts')


# Should weekly schedule
class EmployeeShift(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
