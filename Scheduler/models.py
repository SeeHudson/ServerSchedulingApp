from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import AppUserManager


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    uID = models.CharField(_('user ID'), max_length=9, primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=60, blank=True)
    phone = models.CharField(_('phone number'), max_length=10, blank=True)
    address = models.CharField(_('address'), max_length=100, blank=True)
    city = models.CharField(_('city'), max_length=50, blank=True)
    state = models.CharField(_('state'), max_length=2, blank=True)
    zip_code = models.CharField(_('zip code'), max_length=5, blank=True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['uID']

    objects = AppUserManager()

    def __str__(self):
        return self.email

class Timeoff(models.Model):
    employeeID = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    mondayBegin = models.CharField(_('mondayBegin'), max_length=10, blank=True)
    mondayEnd = models.CharField(_('mondayEnd'), max_length=10, blank=True)
    tuesdayBegin = models.CharField(_('tuesdayBegin'), max_length=10, blank=True)
    tuesdayEnd = models.CharField(_('tuesdayEnd'), max_length=10, blank=True)
    wednesdayBegin = models.CharField(_('wednesdayBegin'), max_length=10, blank=True)
    wednesdayEnd = models.CharField(_('wednesdayEnd'), max_length=10, blank = True)
    thursdayBegin = models.CharField(_('thursdayBegin'), max_length=10, blank=True)
    thursdayEnd = models.CharField(_('thursdayEnd'), max_length=10, blank=True)
    fridayBegin = models.CharField(_('fridayBegin'), max_length=10, blank=True)
    fridayEnd = models.CharField(_('fridayEnd'), max_length=10, blank=True)
    saturdayBegin = models.CharField(_('saturdayBegin'), max_length=10, blank=True)
    saturdayEnd = models.CharField(_('saturdayEnd'), max_length=10, blank=True)
    sundayBegin = models.CharField(_('sundayBegin'), max_length=10, blank=True)
    sundayEnd = models.CharField(_('sundayEnd'), max_length=10, blank=True)

    def __str__(self):
        return self.courseID


class neededShifts(models.Model):
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
    startTime = models.CharField(_('startTime'), max_length=10, blank=True)
    endTime = models.CharField(_('endTime'), max_length=10, blank=True)

    def __str__(self):
        return self.courseID


class UserShift(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    Shift = models.ForeignKey(neededShifts, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email + " " + self.neededShifts.startTime