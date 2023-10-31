from django.db import models

from register.models import CustomUser

class Events(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='eventos/')
    ticketPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    promoter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name