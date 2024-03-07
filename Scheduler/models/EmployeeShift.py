from django.db import models
from django.utils.translation import gettext_lazy as _
from . import Employee
from . import Shift


# Should weekly schedule
class EmployeeShift(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
