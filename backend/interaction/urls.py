from django.urls import path
from .api import LikeAPIView, FeedbackView

urlpatterns = [
   path('/like/<int:api_id>', LikeAPIView.as_view(), name='like-api'),
   path('/feedback', FeedbackView.as_view(), name='feedback')
]
