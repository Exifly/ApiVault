from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from .api import(
     RegisterView,
     CustomTokenObtainPairView,
     ChangePasswordView,
     VerifyEmail,
)

urlpatterns = [
     #LOGIN
     path('login/', CustomTokenObtainPairView.as_view(),
          name='token_obtain_pair'),
     
     #TOKEN
     path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
          name='token_refresh'),
     path('token/verify/', jwt_views.TokenVerifyView.as_view(),
          name='token_verify'),

     #REGISTRATION
     path('register/', RegisterView.as_view()),
     path('email-verify/', VerifyEmail.as_view(), name="email-verify"), 

     #RESET PASSWORD
     path('reset-password/', ChangePasswordView.as_view(), name='reset-password'),

]
