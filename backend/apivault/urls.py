"""apivault URL Configuration"""
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import (
    path,
    include
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('api/', include('vault.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)