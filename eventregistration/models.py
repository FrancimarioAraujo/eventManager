from django.db import models
from event.models import Events, CustomUser

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField(default=1)


