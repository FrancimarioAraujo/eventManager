from django.test import TestCase
from django.urls import reverse

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
    
            

