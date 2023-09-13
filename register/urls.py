from django.urls import path
from . import views

urlpatterns = [
    #path('', views.cadastro, name='cadastro'),
    #path('', views.formulario_cadastro, name='formulario_cadastro'),
    path('', views.register, name='register'),
]