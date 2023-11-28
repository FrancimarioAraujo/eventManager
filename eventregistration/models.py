from django.db import models
from event.models import CustomUser, Events

class Pedido(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    evento = models.ForeignKey(Events, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=254, null=True)
    endereco_entrega = models.CharField(max_length=200)
    cidade_entrega = models.CharField(max_length=100)
    estado_entrega = models.CharField(max_length=50)
    cep_entrega = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=[('Concluído', 'Concluído'), ('Em Processamento', 'Em Processamento')])
    dataCompra = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.username}'

