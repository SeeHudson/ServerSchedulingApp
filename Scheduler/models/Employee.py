from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


# Employee inherits from the User model, includes employee specific fields
class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    # Assuming the employee score is 0-5
    score1 = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    score2 = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    score3 = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    score4 = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    score5 = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    average_score = models.FloatField(default = 0)


    def get_all_shifts_for_employee(self):
        return self.shifts.all()
