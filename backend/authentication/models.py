from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class DefaultUser(AbstractUser):

   class Type(models.TextChoices):
      DEVELOPER = ('D', "DEVELOPER")
      ADMIN = ('A', "ADMIN")

   type = models.CharField(max_length=2, choices=Type.choices, default=Type.DEVELOPER)
   is_verified = models.BooleanField(default=False)

   def tokens(self):
      refresh = RefreshToken.for_user(self)
      return {
         'refresh': str(refresh),
         'access': str(refresh.access_token)
      }


   def __str__(self):
      return self.get_full_name()


   
