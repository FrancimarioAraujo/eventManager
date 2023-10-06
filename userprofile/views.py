from django.shortcuts import render, redirect

def profile(request):
    return render(request, 'meuperfil.html')

def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.fullname = request.POST.get('fullname')
        user.phone = request.POST.get('phone')
        user.email = request.POST.get('email')

        user.save()
        return redirect('profile')

    else:
        return render(request, 'editarmeuperfil.html')
    


