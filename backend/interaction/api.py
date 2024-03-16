# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from .serializers import FeedbackSerializer
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle
from rest_framework import generics
from vault.models import API
from .models import(
    Like,
)

class LikeAPIView(APIView):
   """
   API View to handle liking an API.
   """
   permission_classes = [permissions.IsAuthenticated]
   throttle_classes = [UserRateThrottle]

   def post(self, request, api_id, format=None):
      api = get_object_or_404(API, id=api_id)
      like, created = Like.objects.get_or_create(user=request.user, api=api)

      if created:
         return Response(status=status.HTTP_201_CREATED)
      
      return Response({'detail': 'You have already liked this API.'}, status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request, api_id, format=None):
      api = get_object_or_404(API, id=api_id)
      like, deleted = Like.objects.filter(user=request.user, api=api).delete()

      if deleted:
         return Response(status=status.HTTP_204_NO_CONTENT)
      
      return Response({'detail': 'You have not liked this API yet.'}, status=status.HTTP_400_BAD_REQUEST)


class FeedbackView(generics.CreateAPIView):
   """
   View to handle user feedbacks
   """
   permission_classes = [permissions.IsAuthenticated]
   serializer_class = FeedbackSerializer
   throttle_classes = [UserRateThrottle]

   def perform_create(self, serializer):
      serializer.save(user=self.request.user)
