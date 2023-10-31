from django.shortcuts import render
from event.models import Events
from django.db.models import Q
# Create your views here.

def home(request):
    events = Events.objects.all()
    return render(request, 'home.html', {'events': events})


def search_events(request):
    query = request.GET.get('q')
    search_by = request.GET.get('search_by')

    if search_by == 'name':
        events = Events.objects.filter(name__icontains=query)
    elif search_by == 'category':
        events = Events.objects.filter(category__name__icontains=query)
    else:
        events = Events.objects.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query)
        )

    return render(request, 'search_results.html', {'events': events, 'query': query})