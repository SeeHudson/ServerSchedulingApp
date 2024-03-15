from django.db import models


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=100, null=True, blank=True)

    def get_all_employees(self):
        return self.users.filter(role='EMPLOYEE')

    def get_all_managers(self):
        return self.users.filter(role='MANAGER')

    def get_all_shifts(self):
        employees = self.get_all_employees()
        shifts = []
        for employee in employees:
            shifts += employee.get_all_shifts_for_employee()
        return shifts
