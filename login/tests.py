from django.urls import reverse
from django.test import TestCase, Client
from register.models import CustomUser
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='Carlos369')

    def test_login_user_POST(self):
        response = self.client.post(reverse('login_user'), json.dumps({'username': 'testuser', 'password': 'Carlos369'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'success': True})

    def test_login_user_POST_no_user(self):
        response = self.client.post(reverse('login_user'), json.dumps({'username': 'wrong', 'password': 'wrong'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'Credenciais inválidas'})

    def test_logout_user(self):
        self.client.login(username='testuser', password='Carlos369')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('index'))