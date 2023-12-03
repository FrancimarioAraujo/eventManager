from django.shortcuts import render
from event.models import Events
from django.db.models import Q
from geopy.geocoders import Nominatim

def home(request):
    events = Events.objects.all().filter(status = 'active')
    return render(request, 'home.html', {'events': events})

def search_events(request):
    query = request.GET.get('q')

    events = Events.objects.filter(
        Q(name__icontains=query) | Q(category__name__icontains=query)
    )

    return render(request, 'search_results.html', {'events': events, 'query': query})

def search_location(request):
    query = request.GET.get('location')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    geolocator = Nominatim(user_agent="core")
    location = geolocator.reverse((latitude, longitude))
    print(location)
    
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')

    if city or state:
        events = Events.objects.filter(
            Q(city__icontains=city) & Q(state__icontains = state) 
        )
    else:
        events = Events.objects.filter(
            Q(city__icontains=query) | Q(state__icontains = query) 
        )
    


    return render(request, 'home.html', {'events': events, 'query': query, 'city': city, 'state': state})