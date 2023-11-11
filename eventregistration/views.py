from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Events, Pedido

@login_required
def add_to_cart(request, evento_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            evento = get_object_or_404(Events, pk=evento_id)
            ticket_price = evento.ticket_set.first().ticket_price  

            cart = request.session.get('cart', [])
            found = False
            for item in cart:
                if item['evento_id'] == evento.id:
                    item['quantity'] += quantity
                    found = True
                    break

            if not found:
                cart_item = {'evento_id': evento.id, 'quantity': quantity, 'price': float(ticket_price)}
                cart.append(cart_item)

            request.session['cart'] = cart
            request.session.modified = True

    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = request.session.get('cart', [])
    total = sum(item['quantity'] * item['price'] for item in cart_items)

    return render(request, 'checkout.html', {'items': cart_items, 'total': total})

@login_required
def process_payment(request):
    if request.method == 'POST':
        # Dados do formulário de pagamento
        email = request.POST.get('email')
        endereco = request.POST.get('address')
        cidade = request.POST.get('city')
        estado = request.POST.get('state')
        cep = request.POST.get('zip')


        # Atualiza o banco de dados e crie um pedido relacionado ao usuário
        cart = request.session.get('cart', [])
        total = sum(item['quantity'] * item['price'] for item in cart)
        for item in cart: 
            evento_item = get_object_or_404(Events, pk=item['evento_id'])
            evento = evento_item
            quantidade = item['quantity']

            # Verifique se há ingressos disponíveis
            if evento.ticket_set.filter(qtd_ticket__gte=quantidade).exists():
                # Atualize a quantidade de ingressos no banco de dados
                ingresso = evento.ticket_set.first()
                ingresso.qtd_ticket -= quantidade
                ingresso.save()

                # Cria um pedido relacionado ao usuário
                pedido = Pedido.objects.create(
                    usuario=request.user,  # Substitua isso pelo usuário real
                    evento=evento,
                    quantidade=quantidade,
                    total= total,
                    email=email,
                    endereco_entrega=endereco,
                    cidade_entrega=cidade,
                    estado_entrega=estado,
                    cep_entrega=cep,
                    status='Concluído'  # Pode adicionar mais status se necessário
                )

        # Limpa o carrinho após o pagamento ser concluído
        request.session['cart'] = []
        request.session.modified = True

        # Redireciona para a página de sucesso com informações do pedido
        messages.success(request, 'Compra realizada com sucesso!')
        return redirect('success_page')

    return render(request, 'checkout.html')

@login_required
def success_page(request):
    user = request.user 
    pedido = Pedido.objects.filter(usuario = user).last()
    return render(request, 'order_confirmation.html', {'pedido': pedido})