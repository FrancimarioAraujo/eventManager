from django.shortcuts import render
from event.models import Events

# Create your views here.

def home(request):
    events = Events.objects.all()
    return render(request, 'home.html', {'events': events})