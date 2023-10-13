from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .validators import password_validator, phone_number_validator
import json
from django.http import JsonResponse
from .models import CustomUser

def register(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        username = data.get('username')
        fullname = data.get('fullname')
        phone = data.get('phone')
        email = data.get('email')
        password = data.get('password')
        isPromoter = data.get('isPromoter')


        errors = {}

        if CustomUser.objects.filter(username = username).exists():
            errors['username'] = 'Nome de usuário já existe'

        if CustomUser.objects.filter(email = email).exists():
            errors['email'] = 'Este e-mail já está cadastrado'
 
        if not password_validator(password):
            errors['password'] = 'Sua senha deve possuir pelo menos oito caracteres, incluindo letras maiúsculas e minúsculas e números'
        
        if not phone_number_validator(phone):
            errors['phone'] = 'Número de telefone inváilido'
        
        if not errors:
            user = CustomUser(username=username, fullname=fullname, phone=phone,
                        email=email, password=make_password(password), isPromoter=isPromoter)
            user.save()
            response_data = {'success': True}
            return JsonResponse(response_data)
        else:
            response_data = {'error': errors}
            return JsonResponse(response_data, status=400)

        
    else:
        return render(request, 'cadastro.html')
    

