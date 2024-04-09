from django.db import models
from .Employee import Employee

class Availability(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='availabilities')
    DAY_OF_WEEK_CHOICES = (
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
    )
    SHIFT_TYPE_CHOICES = (
        ('open', 'Open'),
        ('mid', 'Mid'),
        ('close', 'Close'),
    )
    day = models.CharField(max_length=2, choices=DAY_OF_WEEK_CHOICES)
    shift_type = models.CharField(max_length=10, choices=SHIFT_TYPE_CHOICES)

    class Meta:
        unique_together = ('employee', 'day', 'shift_type')

    def __str__(self):
        return f"{self.employee.user.username} - {self.get_day_display()} ({self.get_shift_type_display()})"
