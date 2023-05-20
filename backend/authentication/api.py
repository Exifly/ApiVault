from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from authentication.models import DefaultUser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, response
from django.urls import reverse
from .utils import Util
from .serializer import (
    CustomTokenObtainPairSerializer,
    EmailVerificationSerializer,
    ChangePasswordSerializer,
    RegisterSerializer,
    UserSerializer,
)
import jwt
from django.shortcuts import redirect


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Util.send_email(data=data)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User successfully created.  Now perform Login to get your token",
        }, status=status.HTTP_201_CREATED)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = DefaultUser
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        self.object = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(generics.GenericAPIView):
    serializer_class = EmailVerificationSerializer


    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            print(payload)
            user = DefaultUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return redirect('https://apivault.dev/')
        except jwt.ExpiredSignatureError as identifier:
            return response.Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return response.Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        
 
       
