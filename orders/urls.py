from django.urls import path
from . import views

urlpatterns = [
    path('', views.listOrders, name='listOrders'),
    path('avaliacao/<int:event_id>/', views.avaliar, name='avaliar'),
]