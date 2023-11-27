import json
from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class TestesRegisterView(TestCase):
    

    def test_post_register_view_sucesso(self):
        # Testa a requisição POST para a view de registro com dados válidos
        data = {
            'username': 'testuser',
            'fullname': 'Teste Usuário',
            'phone': '1234567890',
            'email': 'testuser@example.com',
            'password': 'TestPass123',
            'isPromoter': False,
        }
        response = self.client.post(reverse('register'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True})

    def test_post_register_view_username_duplicado(self):
        # Testa a requisição POST para a view de registro com um nome de usuário duplicado
        CustomUser.objects.create(username='existinguser', email='existinguser@example.com')
        data = {
            'username': 'existinguser',
            'fullname': 'Teste Usuário',
            'phone': '1234567890',
            'email': 'testuser@example.com',
            'password': 'TestPass123',
            'isPromoter': False,
        }
        response = self.client.post(reverse('register'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': {'username': 'Nome de usuário já existe'}})

    def test_post_register_view_email_duplicado(self):
        # Testa a requisição POST para a view de registro com um email duplicado
        CustomUser.objects.create(username='existinguser', email='existinguser@example.com')
        data = {
            'username': 'testuser',
            'fullname': 'Teste Usuário',
            'phone': '1234567890',
            'email': 'existinguser@example.com',  # Email duplicado
            'password': 'TestPass123',
            'isPromoter': False,
        }
        response = self.client.post(reverse('register'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': {'email': 'Este e-mail já está cadastrado'}})

    def test_post_register_view_senha_invalida(self):
        # Testa a requisição POST para a view de registro com uma senha inválida
        data = {
            'username': 'testuser',
            'fullname': 'Teste Usuário',
            'phone': '1234567890',
            'email': 'testuser@example.com',
            'password': 'senhafraca',  # Senha inválida
            'isPromoter': False,
        }
        response = self.client.post(reverse('register'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': {'password': 'Sua senha deve possuir pelo menos oito caracteres, incluindo letras maiúsculas e minúsculas e números'}})

    def test_post_register_view_telefone_invalido(self):
        # Testa a requisição POST para a view de registro com um telefone inválido
        data = {
            'username': 'testuser',
            'fullname': 'Teste Usuário',
            'phone': '123',  # Telefone inválido
            'email': 'testuser@example.com',
            'password': 'TestPass123',
            'isPromoter': False,
        }
        response = self.client.post(reverse('register'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': {'phone': 'Número de telefone inváilido'}})

    def test_post_register_view_usuario_existente(self):
        # Testa a requisição POST para a view de registro com um usuário existente
        CustomUser.objects.create(username='existinguser', email='existinguser@example.com')
        data = {
            'username': 'existinguser',
            'fullname': 'Teste Usuário',
            'phone': '1234567890',
            'email': 'testuser@example.com',
            'password': 'TestPass123',
            'isPromoter': False,
        }
        response = self.client.post(reverse('register'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': {'username': 'Nome de usuário já existe'}})
