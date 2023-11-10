from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem, Events, Order
from django.utils import timezone
from datetime import datetime


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
    return render(request, 'checkcout.html', {'items': items, 'total': total})


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return redirect('view_cart')


def checkout(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=sum(item.event.ticketPrice *
                            item.quantity for item in cart_items),
        )
        order.items.set(cart_items)

        # Limpe o carrinho
        user_cart.order = order
        user_cart.save()

        return redirect('page_success')
    
    else:
        return render(request, 'checkout.html')

def page_success(request):
    return render(request, 'pagina_de_confirmacao.html')
