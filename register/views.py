from .models import User
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .validators import UppercaseLowercaseDigitValidator, phoneNumberValidator
from django.contrib import messages
import json
from django.shortcuts import redirect
from django.http import JsonResponse


def register(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        username = data.get('username')
        fullname = data.get('fullname')
        phone = data.get('phone')
        email = data.get('e-mail')
        password = data.get('password')
        isPromoter = data.get('isPromoter')
    
        

       
        #Cria um novo usuário
        user = User(username=username, fullname=fullname, phone=phone,
                    email=email, password=make_password(password), isPromoter=isPromoter)
        user.save()
        response_data = {'success': True}
        return JsonResponse(response_data)
    
    else:
        return render(request, 'cadastro.html', {'messages': messages.get_messages(request)})
    

