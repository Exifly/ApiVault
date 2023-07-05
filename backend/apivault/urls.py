"""apivault URL Configuration"""
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import (
    path,
    include,
    re_path
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('vault.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/interaction', include('interaction.urls')),

    #documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)