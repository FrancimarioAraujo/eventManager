from django.shortcuts import render
from django.contrib.auth.hashers import make_password
import json
from django.http import JsonResponse
from django.db import IntegrityError
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
        
        try:
            user = CustomUser(username=username, fullname=fullname, phone=phone,
                        email=email, password=make_password(password), isPromoter=isPromoter)
            user.save()
            response_data = {'success': True}
            return JsonResponse(response_data)
        except IntegrityError as e:
            response_data = {'error': f'Erro: {e}'}
            return JsonResponse({'error': errors}, status=400)

        
    else:
        return render(request, 'cadastro.html')
    

