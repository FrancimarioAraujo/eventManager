from django.db import models
from register.models import CustomUser

class EventCategory(models.Model):
    name = models.CharField(max_length = 50, unique= True)

    def __str__(self):
        return self.name

class Events(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    capacity = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='eventos/')
    category = models.ForeignKey(EventCategory, null=True, on_delete = models.DO_NOTHING)
    promoter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    ACTIVE = 'active'
    CLOSED = 'closed'
    EVENT_STATUS_CHOICES = [(ACTIVE, 'Active'), (CLOSED, 'Closed')]

    status = models.CharField(max_length=10, choices=EVENT_STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_ticket = models.PositiveIntegerField()

    def __str__(self):
        return f'Ingresso para {self.event.name}'