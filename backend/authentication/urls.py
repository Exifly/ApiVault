from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from .api import(
     GoogleSocialAuthView,
)

urlpatterns = [
     #TOKEN
     path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
          name='token_refresh'),
     path('token/verify/', jwt_views.TokenVerifyView.as_view(),
          name='token_verify'),

     path('google/', GoogleSocialAuthView.as_view()),

]
