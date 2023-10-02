from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client

class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = Client()

    def test_valido_login(self):
       
        response = self.client.post(reverse('login_user'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['successo'], True)

    def test_invalido_login(self):
        
        response = self.client.post(reverse('login_user'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'credenciais inválidas')

class LogoutUserTestCase(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = Client()
        

    def test_logout_user(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
