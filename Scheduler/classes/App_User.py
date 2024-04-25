from Scheduler.models import User, Employee


class AppUserClass:
    def __init__(self, email="", password="", first_name="", last_name="",
                 phone_number="", address="", city="", state="", zip_code=""):
        self.user = None
        if email:  # If email is provided, create a new user
            self.user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            self.user.phone = phone_number
            self.user.address = address
            self.user.city = city
            self.user.state = state
            self.user.zip_code = zip_code
            self.user.save()

    def getUID(self):
        if self.uID == "":
            raise TypeError("No uID assigned to user.")
        else:
            return self.UID

    def get_email(self):
        return self.user.email if self.user else None

    def set_email(self, email):
        if self.user:
            self.user.email = email
            self.user.save()

    def get_first_name(self):
        return self.user.first_name if self.user else None

    def set_first_name(self, first_name):
        if self.user:
            self.user.first_name = first_name
            self.user.save()

    def get_last_name(self):
        return self.user.last_name if self.user else None

    def set_last_name(self, last_name):
        if self.user:
            self.user.last_name = last_name
            self.user.save()

    def get_phone_number(self):
        return self.user.phone if self.user else None

    def set_phone_number(self, phone_number):
        if self.user:
            self.user.phone = phone_number
            self.user.save()

    def get_address(self):
        return self.user.address if self.user else None

    def set_address(self, address):
        if self.user:
            self.user.address = address
            self.user.save()

    def get_city(self):
        return self.user.city if self.user else None

    def set_city(self, city):
        if self.user:
            self.user.city = city
            self.user.save()

    def get_state(self):
        return self.user.state if self.user else None

    def set_state(self, state):
        if self.user:
            self.user.state = state
            self.user.save()

    def get_zip_code(self):
        return self.user.zip_code if self.user else None

    def set_zip_code(self, zip_code):
        if self.user:
            self.user.zip_code = zip_code
            self.user.save()
