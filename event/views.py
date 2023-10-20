from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpResponse
from .models import Events
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404



def viewEvent(request, evento_id):
    evento = get_object_or_404(Events, pk=evento_id)
    return render(request, 'pagina_evento.html', {'evento': evento})

@login_required
def listEvent(request):
    promoter = request.user
    eventos = Events.objects.all().filter(promoter = promoter)
    return render(request, 'meuseventos.html', {'eventos': eventos})

@login_required
def createEvent(request):
    if not request.user.isPromoter:
        return HttpResponse('Você não tem permissão para acessar essa página')

    if request.method == 'POST':
        promoter = request.user
        nameEvent = request.POST.get('nameEvent')
        address = request.POST.get('address')
        dateTime = request.POST.get('dateTime')
        price = request.POST.get('ticketPrice')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        dateTime = timezone.make_aware(timezone.datetime.strptime(dateTime, "%Y-%m-%dT%H:%M"))

        if not Events.objects.filter(name = nameEvent).exists():
            event = Events(name=nameEvent, address=address, date=dateTime, description=description, image=image, ticketPrice=price, promoter=promoter)
            event.save()
            messages.success(request, 'Evento criado com sucesso!')

            return redirect('createEvent')
        else:

            return render(request, 'cadastrareventos.html', {'nameError': True})

    else:
        return render(request, 'cadastrareventos.html')
    
@login_required
def editEvent(request, event_id):
    event = Events.objects.get(id=event_id)

    if request.user != event.promoter:
        return HttpResponse('Você não tem permissão para editar este evento')

    if request.method == 'POST':
        event.name = request.POST.get('nameEvent')
        event.address = request.POST.get('address')
        event.date = timezone.make_aware(timezone.datetime.strptime(request.POST.get('dateTime'), "%Y-%m-%dT%H:%M"))
        event.description = request.POST.get('description')
        event.ticketPrice = request.POST.get('ticketPrice')

        if request.FILES.get('image'):
            event.image = request.FILES.get('image')
        event.save()
        messages.success(request, 'Evento editado com sucesso!')
        return redirect('listEvent')

    return render(request, 'editarevento.html', {'event': event})


@login_required
def deleteEvent(request, event_id):
    event = Events.objects.get(id=event_id)

    if request.user != event.promoter:
        return HttpResponse('Você não tem permissão para excluir este evento')

    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Evento excluído com sucesso!')
        return redirect('listEvent')

    return render(request, 'excluirevento.html', {'event': event})
