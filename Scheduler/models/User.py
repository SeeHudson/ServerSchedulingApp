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
