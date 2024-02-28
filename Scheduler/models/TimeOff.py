from django.db import models
from django.utils.translation import gettext_lazy as _
from . import Employee


# Have to go over this and availability
class Timeoff(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)

    mondayBegin = models.CharField(_('mondayBegin'), max_length=10, blank=True)
    mondayEnd = models.CharField(_('mondayEnd'), max_length=10, blank=True)
    tuesdayBegin = models.CharField(_('tuesdayBegin'), max_length=10, blank=True)
    tuesdayEnd = models.CharField(_('tuesdayEnd'), max_length=10, blank=True)
    wednesdayBegin = models.CharField(_('wednesdayBegin'), max_length=10, blank=True)
    wednesdayEnd = models.CharField(_('wednesdayEnd'), max_length=10, blank=True)
    thursdayBegin = models.CharField(_('thursdayBegin'), max_length=10, blank=True)
    thursdayEnd = models.CharField(_('thursdayEnd'), max_length=10, blank=True)
    fridayBegin = models.CharField(_('fridayBegin'), max_length=10, blank=True)
    fridayEnd = models.CharField(_('fridayEnd'), max_length=10, blank=True)
    saturdayBegin = models.CharField(_('saturdayBegin'), max_length=10, blank=True)
    saturdayEnd = models.CharField(_('saturdayEnd'), max_length=10, blank=True)
    sundayBegin = models.CharField(_('sundayBegin'), max_length=10, blank=True)
    sundayEnd = models.CharField(_('sundayEnd'), max_length=10, blank=True)
