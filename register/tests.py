from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterTestCase(TestCase):

    def test_register_post(self):
        

        data = {
            'username': 'usuario_teste',
            'fullname': 'nome completo',
            'phone': '12345678901',
            'e-mail': 'teste@email.com',
            'password': 'Senha123',
            'isPromoter': 'true',
        }

        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code, 200)


    
    def test_duplicate_username(self):
        User.objects.create_user(username='usuario_teste', password='Senha123', email='teste@email.com')

        new_user_data = {
            'username': 'usuario_teste',
            'fullname': 'novo nome completo',
            'phone': '9876543210',
            'e-mail': 'novo@email.com',
            'password': 'NovaSenha123',
            'isPromoter': 'false',
        }

        response = self.client.post(reverse('register'), new_user_data)

        self.assertEqual(response.status_code, 200)


    def test_duplicate_email(self):
        User.objects.create_user(username='usuario_teste', password='Senha123', email='teste@email.com')
        
        new_user_data = {
            'username': 'novo_usuario',
            'fullname': 'novo nome completo',
            'phone': '9876543210',
            'e-mail': 'teste@email.com',
            'password': 'NovaSenha123',
            'isPromoter': 'false',
        }
        response = self.client.post(reverse('register'), new_user_data)

        self.assertEqual(response.status_code, 200)

    

    
        


        

        

        


    
            

