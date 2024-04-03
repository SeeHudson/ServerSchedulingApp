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
        return self.user.phone

    def set_phone_number(self, phone_number):
        self.user.phone_number = phone_number
        self.user.save()

    def get_address(self):
        return self.user.address

    def set_address(self, address):
        self.user.address = address
        self.user.save()

    def get_city(self):
        return self.user.city

    def set_city(self, city):
        self.user.city = city
        self.user.save()

    def get_state(self):
        return self.user.state

    def set_state(self, state):
        self.user.state = state
        self.user.save()

    def get_zip_code(self):
        return self.user.zip_code

    def set_zip_code(self, zip_code):
        self.user.zip_code = zip_code
        self.user.save()