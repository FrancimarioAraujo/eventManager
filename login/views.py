from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json


def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        username = data.get('username')
        password = data.get('password')


        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            response_data = {'success': True}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Credenciais inválidas'}, status=400)
        
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')