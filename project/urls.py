from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from django.views.generic import RedirectView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/')),
    path('home/', include('core.urls')),
    path('cadastro/', include('register.urls')),
    path('login/', include('login.urls')),
    path('profile/', include('userprofile.urls')),
    path('eventos/', include('event.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)