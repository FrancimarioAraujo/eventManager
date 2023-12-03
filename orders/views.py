from django.shortcuts import render, redirect
from eventregistration.models import Pedido
from event.models import Events
from .models import AvaliarEvento
from django.contrib.auth.decorators import login_required

@login_required
def listOrders(request):
    user = request.user
    pedido = Pedido.objects.filter(usuario = user)
    return render(request, 'my-orders.html', {'pedido': pedido})

@login_required
def avaliar(request, event_id):
    user = request.user
    event = Events.objects.get(pk=event_id)
    if request.method == 'POST':
        titulo = request.POST.get('title')
        descricao = request.POST.get('description')
        qualidade = request.POST.get('quality')
        recomendacao = request.POST.get('recomendation')

        avaliar = AvaliarEvento(usuario = user ,evento = event, titulo = titulo, descricao = descricao, 
                                qualidade = qualidade, recomendacao = recomendacao)
        avaliar.save()
        
        return redirect('viewEvent', event_id)
    
    return render(request, 'avaliar.html', {'event': event})

