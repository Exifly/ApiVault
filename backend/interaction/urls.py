from django.urls import path
from .api import LikeAPIView

urlpatterns = [
   path('/like/<int:api_id>/', LikeAPIView.as_view(), name='like-api'),
]
