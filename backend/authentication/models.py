from django.db import models
from django.contrib.auth.models import AbstractUser


class DefaultUser(AbstractUser):

   class Type(models.TextChoices):
      DEVELOPER = ('D', "DEVELOPER")
      ADMIN = ('A', "ADMIN")

   type = models.CharField(max_length=2, choices=Type.choices, default=Type.DEVELOPER)
   is_verified = models.BooleanField(default=False)


   def __str__(self):
      return self.get_full_name()


   
