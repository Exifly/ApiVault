from rest_framework.exceptions import AuthenticationFailed
from authentication.models import DefaultUser
from .register import register_social_user
from rest_framework import serializers
from apivault import settings
from . import google


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']

        return register_social_user(email=email, name=name)


# User serializer
class UserSerializer(serializers.ModelSerializer):
    """A safe Serializer of the default django auth user model"""
    class Meta:
        model = DefaultUser
        fields = ['id', 'email', 'first_name', 'last_name',
                  'date_joined', 'onboarding_done', 'is_verified']


class SafeUserSerializer(serializers.ModelSerializer):
    """A safe Serializer of the default django auth user model"""
    class Meta:
        model = DefaultUser
        fields = ['first_name', 'last_name', 'email', 'is_verified']



class UserSerializerNotSafe(serializers.ModelSerializer):
    """WARNING: Debug purpose only.
    DO NOT USE IT IN PRODUCTION"""
    class Meta:
        model = DefaultUser
        fields = '__all__'