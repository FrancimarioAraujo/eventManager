from django.db import models
from event.models import Events
from register.models import CustomUser

class AvaliarEvento(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    evento = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    qualidade = models.PositiveIntegerField()
    recomendacao = models.BooleanField()

