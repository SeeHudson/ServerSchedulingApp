from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist


# Users inherit usual fields like username, password, etc. from the AbstractUser class + role field
class User(AbstractUser):
    ROLE_CHOICES = (
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True, related_name='users')

    # Create role when user is created
    #Might need to add phone number, address
    email = models.EmailField('email', max_length=100, blank=True)
    phone = models.CharField('phone', max_length=10, blank=True)
    address = models.CharField('address', max_length=100, blank=True)
    city = models.CharField('city', max_length=50, blank=True)
    state = models.CharField('state', max_length=2, blank=True)
    zip_code = models.CharField('zip code', max_length=5, blank=True)

    # Create role when user is created
    # Might need to add phone number, address
    def set_email(self, email):
        self.email = email
        self.save()

    def set_first_name(self, first_name):
        self.first_name = first_name
        self.save()

    def set_last_name(self, last_name):
        self.last_name = last_name
        self.save()

    def set_phone_number(self, phone_number):
        try:
            self.phone = phone_number
            self.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def set_address(self, address):
        try:
            self.address = address
            self.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def set_city(self, city):
        try:
            self.city = city
            self.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def set_state(self, state):
        try:
            self.state = state
            self.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def set_zip_code(self, zip_code):
        try:
            self.zip_code = zip_code
            self.save()
        except ObjectDoesNotExist:
            return None