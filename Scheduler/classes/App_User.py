from Scheduler.models import User, Employee, Manager
from django.core.exceptions import ObjectDoesNotExist


class AppUserClass:
    def __init__(self, email="", password="", first_name="", last_name="",
                 phone_number="", address="", city="", state="", zip_code=""):
        # Check if user exists first
        try:
            user = User.objects.get(email=email)
            self.user = user
        except ObjectDoesNotExist:
            # Need to make a new user
            if email == "" or password == "":
                raise ValueError("Email and password are required")
            else:
                user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
                user.role = 'EMPLOYEE'  # Assuming default role is employee
                user.save()
                self.user = user

    def get_email(self):
        return self.user.email

    def set_email(self, email):
        self.user.email = email
        self.user.save()

    def get_first_name(self):
        return self.user.first_name

    def set_first_name(self, first_name):
        self.user.first_name = first_name
        self.user.save()

    def get_last_name(self):
        return self.user.last_name

    def set_last_name(self, last_name):
        self.user.last_name = last_name
        self.user.save()

    def get_phone_number(self):
        try:
            employee = Employee.objects.get(user=self.user)
            return employee.phone_number
        except ObjectDoesNotExist:
            return None

    def set_phone_number(self, phone_number):
        try:
            employee = Employee.objects.get(user=self.user)
            employee.phone_number = phone_number
            employee.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def get_address(self):
        try:
            employee = Employee.objects.get(user=self.user)
            return employee.address
        except ObjectDoesNotExist:
            return None

    def set_address(self, address):
        try:
            employee = Employee.objects.get(user=self.user)
            employee.address = address
            employee.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def get_city(self):
        try:
            employee = Employee.objects.get(user=self.user)
            return employee.city
        except ObjectDoesNotExist:
            return None

    def set_city(self, city):
        try:
            employee = Employee.objects.get(user=self.user)
            employee.city = city
            employee.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def get_state(self):
        try:
            employee = Employee.objects.get(user=self.user)
            return employee.state
        except ObjectDoesNotExist:
            return None

    def set_state(self, state):
        try:
            employee = Employee.objects.get(user=self.user)
            employee.state = state
            employee.save()
        except ObjectDoesNotExist:
            return None  # Employee doesn't exist

    def get_zip_code(self):
        try:
            employee = Employee.objects.get(user=self.user)
            return employee.zip_code
        except ObjectDoesNotExist:
            return None

    def set_zip_code(self, zip_code):
        try:
            employee = Employee.objects.get(user=self.user)
            employee.zip_code = zip_code
            employee.save()
        except ObjectDoesNotExist:
            return None
