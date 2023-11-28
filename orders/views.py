from django.shortcuts import render
from eventregistration.models import Pedido
from django.contrib.auth.decorators import login_required

@login_required
def listOrders(request):
    user = request.user
    pedido = Pedido.objects.filter(usuario = user)
    return render(request, 'my-orders.html', {'pedido': pedido})

