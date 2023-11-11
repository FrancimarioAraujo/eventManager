from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name= 'view_cart'),
    path('add_to_cart/<int:evento_id>/', views.add_to_cart, name='add_to_cart'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('success', views.success_page, name='success_page')
]