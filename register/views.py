from .models import User
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .validators import UppercaseLowercaseDigitValidator, phoneNumberValidator
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['e-mail']
        password = request.POST['password']
        isPromoter_str = request.POST.get('isPromoter')
        if isPromoter_str:
            isPromoter = isPromoter_str.lower() == 'true'
        else:
            isPromoter = False
        

        #Verifica se o e-mail e username já estão cadastado
        error_message = {}
        if User.objects.filter(username=username).exists():
            error_message['username'] = "Username já cadastrado."
            return render(request, 'cadastro.html', {'error_message': error_message, 'username': username})
        if User.objects.filter(email=email).exists():
            error_message['email'] = "E-mail já está em uso."
            return render(request, 'cadastro.html', {'error_message': error_message, 'email': email})

        #Valida a senha do usuário
        validator = UppercaseLowercaseDigitValidator(min_digits=1, min_lower=1, min_upper=1)
        try:
            validator(password)
        except ValidationError as e:
            error_message['email'] = 'Sua senha deve possuir pelo menos oito caracteres, incluindo letras maiúsculas e minúsculas e números'
            return render(request, 'cadastro.html', {'error_message': error_message, 'password': password})
        
        #Verifica se o número de telefone é valido
        validatorPhone = phoneNumberValidator.validate_phone_number(phone)
        try:
            validatorPhone
        except ValidationError as e :
            error_message['phone'] = 'O número de telefone não é válido. Certifique-se de incluir apenas números'
            return render(request, 'cadastro.html', {'error_message': error_message, 'phone': phone})
        
        #Cria um novo usuário
        user = User(username=username, fullname=fullname, phone=phone,
                    email=email, password=make_password(password), isPromoter=isPromoter)
        user.save()
        return render(request, 'cadastroRealizado.html')
    
    else:
        return render(request, 'cadastro.html', {'messages': messages.get_messages(request)})

