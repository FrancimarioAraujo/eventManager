from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('cadastro/', include('register.urls')),
    path('login/', include('login.urls')),
    path('profile/', include('userprofile.urls')),
]