from django.db import models
from event.models import Events, CustomUser


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    #date = models.DateTimeField()

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, null=True, blank=True, on_delete=models.SET_NULL)

class CheckoutForm(models.Model):
    payment_method = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)