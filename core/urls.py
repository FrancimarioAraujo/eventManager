from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('search/', views.search_events, name='search_events'),
]