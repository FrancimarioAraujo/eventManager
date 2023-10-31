from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem, Events

def add_to_cart(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    quantity = request.POST.get('quantity')
    print(quantity)

    item, created = CartItem.objects.get_or_create(cart=user_cart, event=event)
    if not created:
        item.quantity = quantity
        item.save()

    return redirect('view_cart')

def view_cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=user_cart)
    total = sum(item.event.ticketPrice * item.quantity for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return redirect('view_cart')
