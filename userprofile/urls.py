from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
]