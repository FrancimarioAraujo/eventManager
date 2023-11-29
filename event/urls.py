from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:evento_id>/', views.viewEvent, name='viewEvent'),
    path('create/', views.createEvent, name='createEvent'),
    path('myevents/', views.listEvent, name='listEvent'),
    path('edit-event/<int:event_id>/', views.editEvent, name='editEvent'),
    path('delete-event/<int:event_id>/', views.deleteEvent, name='delEvent'),
    path('close-event/<int:event_id>/', views.closeEvent, name='closeEvent'),
]

