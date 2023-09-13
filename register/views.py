from .models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .validators import UppercaseLowercaseDigitValidator

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
        if User.objects.filter(username=username).exists():
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            return redirect('register')

        #Valida a senha do usuário
        validator = UppercaseLowercaseDigitValidator(min_digits=1, min_lower=1, min_upper=1)
        try:
            validator(password)
        except ValidationError as e:
            #return render(request, 'cadastro.html', {'error_message': str(e)})
            return HttpResponse(str(e), status=400)
        
        #Cria um novo usuário
        user = User(username=username, fullname=fullname, phone=phone,
                    email=email, password=make_password(password), isPromoter=isPromoter)
        user.save()
        return render(request, 'cadastroRealizado.html')
    
    else:
        return render(request, 'cadastro.html')


