from django.db import models
from django.contrib.auth.models import AbstractUser
from . import Manager
from . import Employee


# Users inherit usual fields like username, password, etc. from the AbstractUser class + role field
class User(AbstractUser):
    ROLE_CHOICES = (
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    # Create role when user is created

