"""apivault URL Configuration"""
from drf_spectacular.views import SpectacularSwaggerView
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import (
    path,
    include,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('vault.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/interaction', include('interaction.urls')),

    #documentation
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)