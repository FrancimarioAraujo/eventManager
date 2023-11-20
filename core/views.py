from django.shortcuts import render
from event.models import Events
from django.db.models import Q

def home(request):
    events = Events.objects.all()
    return render(request, 'home.html', {'events': events})


def search_events(request):
    query = request.GET.get('q')

    events = Events.objects.filter(
        Q(name__icontains=query) | Q(category__name__icontains=query)
    )

    return render(request, 'search_results.html', {'events': events, 'query': query})