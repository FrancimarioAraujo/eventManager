from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpResponse
from .models import Events, EventCategory, Ticket
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .validatros import validar_imagem

def viewEvent(request, evento_id):
    evento = get_object_or_404(Events, pk=evento_id)
    ticket = Ticket.objects.filter(event= evento_id)[0]
    return render(request, 'pagina_evento.html', {'evento': evento, 'ticket': ticket.ticket_price})

@login_required
def listEvent(request):
    promoter = request.user
    eventos = Events.objects.all().filter(promoter = promoter)
    return render(request, 'meuseventos.html', {'eventos': eventos})

@login_required
def createEvent(request):
    if not request.user.isPromoter:
        return HttpResponse('Você não tem permissão para acessar essa página')
    
    categories = EventCategory.objects.all()

    if request.method == 'POST':
        promoter = request.user
        nameEvent = request.POST.get('nameEvent')
        description = request.POST.get('description')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        capacity = request.POST.get('capacity')
        price = request.POST.get('ticketPrice')
        image = request.FILES.get('image')
        start_date = timezone.make_aware(timezone.datetime.strptime(start_date, "%Y-%m-%dT%H:%M"))
        end_date = timezone.make_aware(timezone.datetime.strptime(end_date, "%Y-%m-%dT%H:%M"))

        category_id = request.POST.get('category')
        category = EventCategory.objects.get(id=category_id)

        # Verifica o tamno da imagem e sua extenção
        # if validar_imagem(image):
        #     return render(request, 'cadastrareventos.html', {'imageError': True})
    
        if not Events.objects.filter(name = nameEvent).exists():
            event = Events(name=nameEvent, address=address, city=city, state=state, start_date=start_date, 
                           end_date=end_date, capacity=capacity, description=description, image=image, 
                           promoter=promoter, category=category)
            event.save()
            # Criação de ingressos associados ao evento
            ticket = Ticket(event=event, ticket_price=price, qtd_ticket=capacity)
            ticket.save()

            messages.add_message(request, constants.SUCCESS, 'Evento criado com sucesso!')

            return redirect('listEvent')
        else:
            return render(request, 'cadastrareventos.html', {'categories': categories, 'nameError': True})

    else:
        return render(request, 'cadastrareventos.html', {'categories': categories})
    
@login_required
def editEvent(request, event_id):
    event = Events.objects.get(id=event_id)
    ticket = Ticket.objects.get(event=event)

    if request.user != event.promoter:
        return HttpResponse('Você não tem permissão para editar este evento')

    if request.method == 'POST':
        capacity = int(request.POST.get('capacity'))
        ticket_price = request.POST.get('ticketPrice')

        event.name = request.POST.get('nameEvent')
        event.address = request.POST.get('address')
        event.city = request.POST.get('city')
        event.state = request.POST.get('state')
        event.start_date = timezone.make_aware(timezone.datetime.strptime(request.POST.get('start_date'), "%Y-%m-%dT%H:%M"))
        event.end_date = timezone.make_aware(timezone.datetime.strptime(request.POST.get('end_date'), "%Y-%m-%dT%H:%M"))
        event.capacity = capacity
        event.description = request.POST.get('description')
        ticket.ticket_price = ticket_price

        if request.FILES.get('image'):
            event.image = request.FILES.get('image')
        event.save()

        capacity_difference = capacity - event.capacity
        if ticket:
            ticket.ticket_price = ticket_price
            ticket.qtd_ticket = max(0, ticket.qtd_ticket + capacity_difference)
            ticket.save()
            
        messages.success(request, 'Evento editado com sucesso!')
        return redirect('listEvent')

    return render(request, 'editarevento.html', {'event': event})


@login_required
def deleteEvent(request, event_id):
    event = Events.objects.get(id=event_id)

    if request.user != event.promoter:
        return HttpResponse('Você não tem permissão para excluir este evento')

    if request.method == 'POST':
        if event.image:
            event.image.delete()

        tickets = Ticket.objects.filter(event=event)
        for ticket in tickets:
            ticket.delete()
            
        event.delete()
        messages.success(request, 'Evento excluído com sucesso!')
        return redirect('listEvent')

    return render(request, 'excluirevento.html', {'event': event})

@login_required
def closeEvent(request, event_id):
    event = Events.objects.get(pk=event_id)

    if event.end_date < timezone.now():
        event.status = Events.CLOSED
        event.save()
    
        return redirect('viewEvent', event_id)
    

    return render(request, 'meuseventos.html')

