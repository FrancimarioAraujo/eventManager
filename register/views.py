import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def cadastro(request):
    return render(request, 'cadastro.html')

@csrf_protect
def formulario_cadastro(request):
    if request.method == 'POST':
        #Obtendo os dados do formulário
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['e-mail']
        password = request.POST['password']
        
        dados = {
            'username': username,
            'first_name': firstname,
            'last_name': lastname,
            'phone': phone,
            'email': email,
            'password': password,
         }

        # Fazer a chamada POST para a API
        api_url = 'http://localhost:8080/api/v1/register/'
        response = requests.post(api_url, data=dados)

        if response.status_code == 201:
            return HttpResponse('Cadastrado com sucesso!')
        else:
            return HttpResponse('Erro')
        
    return render(request, 'cadastro.html')


