from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from register.validators import password_validator

def profile(request):
    return render(request, 'meuperfil.html')


def update_password(user, current_password, new_password):
    if user.check_password(current_password):
        user.set_password(new_password)
        return True
    return False

def update_user_data(user, request):
    user.username = request.POST.get('username')
    user.fullname = request.POST.get('fullname')
    user.phone = request.POST.get('phone')
    user.email = request.POST.get('email')
    user.save()

def update_profile(request):
    if request.method == 'POST':
        user = request.user

        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if new_password:
            if not password_validator(new_password):
                return render(request, 'editarmeuperfil.html', {'password_invalid_error': True})
            if new_password == confirm_new_password:
                if update_password(user, current_password, new_password):
                    update_session_auth_hash(request, user)
                else:
                    return render(request, 'editarmeuperfil.html', {'current_password_error': True})
            else:
                return render(request, 'editarmeuperfil.html', {'password_mismatch_error': True})
           
        
        update_user_data(user, request)       
        messages.success(request, 'Perfil atualizado com sucesso.')
        return redirect('profile')
            
    else:
        return render(request, 'editarmeuperfil.html')
    


