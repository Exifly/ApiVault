from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializer import (
    GoogleSocialAuthSerializer,
    SafeUserSerializer
)

class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get user information
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
    

class UserView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SafeUserSerializer

    def get(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get user information
        """
        serializer = SafeUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
