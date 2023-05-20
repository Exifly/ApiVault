from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import update_last_login
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueValidator
from authentication.models import DefaultUser
from rest_framework import serializers



# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=DefaultUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = DefaultUser
        fields = ['username','password', 'password2',
                'email', 'first_name', 'last_name', 'type']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs


    def create(self, validated_data):
        user = DefaultUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            type = validated_data['type'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user



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



class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    model = DefaultUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'is_verified': self.user.is_verified})
        data.update({'type': self.user.type})
        data.update({'last_login': self.user.last_login})
        data.update({'onboarding_done': self.user.onboarding_done})
        update_last_login(None, self.user)
        return data
    

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = DefaultUser
        fields = ['token']