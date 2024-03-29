from django.db import models
from django.contrib.auth.models import AbstractUser


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
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    phone = models.CharField('phone number', max_length=10, blank=True)
    address = models.CharField('address', max_length=100, blank=True)
    city = models.CharField('city', max_length=50, blank=True)
    state = models.CharField('state', max_length=2, blank=True)
    zip_code = models.CharField('zip code', max_length=5, blank=True)