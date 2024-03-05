from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


#from Scheduler.models import AppUser
#from classes import __init__

class TestLogin(TestCase):
    def setup(self):
        self.client = Client()
        self.email = 'test@example.com'
        self.password = 'password123'
        self.user = User.objects.create_user(username='testuser', email=self.email, password=self.password)
    def test_validLogin(self):
        #Already added user information
        email_attempt = "test@example.com"
        password_attempt = "testpassword"
        response = self.client.post('login/', {'email': email_attempt, 'password': password_attempt})
        self.assertRedirects(response, '') #index??

    def test_invalidEmail(self):
        # Test case 2: Invalid email
        response = self.client.post('login/', {'email': 'invalid@email.com', 'password': 'testpassword'})
        self.assertContains(response, 'Invalid email or password')


    def test_invalidPassword(self):
        # Test case 3: Invalid password
        response = self.client.post('login/', {'email': 'test@example.com', 'password': 'wrongpassword'})
        self.assertContains(response, 'Invalid email or password')