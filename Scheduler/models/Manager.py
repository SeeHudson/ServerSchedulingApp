from django.db import models
from django.conf import settings


# Manager inherits from the User model, includes manager specific fields
class Manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
