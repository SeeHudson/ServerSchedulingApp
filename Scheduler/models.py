from django.db import models
# Create your models here.
# starting idea for DB imp in models
class Server(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

class Shift(models.Model):
    date = models.DateField(auto_now_add=True, primary_key=True)
    shift_type = models.CharField(max_length=50)
    shift_weight = models.IntegerField()

class Shifts(models.Model):
    shift_server_id = models.AutoField(primary_key=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, to_field='email')
    server_score = models.IntegerField()

class WeeklySchedule(models.Model):
    week_start_date = models.DateField(auto_now_add=True, primary_key=True)
    shift = models.ForeignKey(Shifts, on_delete=models.CASCADE)

class Availability(models.Model):
    shift = models.CharField(max_length=50, primary_key=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, to_field='email')
    available = models.BooleanField()