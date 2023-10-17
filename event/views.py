from django.shortcuts import render

def createEvent(request):
    if request.method == 'POST':
        return render(request, 'cadastrareventos.html')
    else:
        pass