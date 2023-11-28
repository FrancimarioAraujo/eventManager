from django.shortcuts import render
from event.models import Events
from django.db.models import Q
from django.http import JsonResponse

def home(request):
    events = Events.objects.all()
    return render(request, 'home.html', {'events': events})


def search_events(request):
    query = request.GET.get('q')

    events = Events.objects.filter(
        Q(name__icontains=query) | Q(category__name__icontains=query)
    )

    return render(request, 'search_results.html', {'events': events, 'query': query})

def search_location(request):
    query = request.GET.get('location')

    events = Events.objects.filter(
        Q(city__icontains=query) |  Q(state__icontains = query)
    )

    return render(request, 'home.html', {'events': events, 'query': query})