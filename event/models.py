from django.db import models
from register.models import CustomUser

class EventCategory(models.Model):
    name = models.CharField(max_length = 50, unique= True)

    def __str__(self):
        return self.name

class Events(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='eventos/')
    ticketPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    capacity = models.PositiveIntegerField()
    category = models.ForeignKey(EventCategory, null=True, on_delete = models.DO_NOTHING)
    promoter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name