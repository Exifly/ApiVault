from authentication.models import DefaultUser
from django.contrib.auth import authenticate
import random

def generate_username(name):
   """
   Generates a username based on the given name.
   Args:
      name (str): The user's name.
   Returns:
      str: The generated username.
   """
   
   username = "".join(name.split(' ')).lower()
   return username + str(random.randint(0, 1000))

def register_social_user(email, name):
   """
   Registers a social user.

   If the user does not exist, a new user is created with the provided email, name, and a default password.
   The user is then authenticated and the relevant user information is returned.

   Args:
      email (str): The user's email.
      name (str): The user's name.

   Returns:
      dict: A dictionary containing the registered user's username, email, and tokens.
   """

   user = DefaultUser.objects.filter(email=email).first()

   if not user:
      user = DefaultUser.objects.create_user(
         username=generate_username(name),
         email=email,
         password="pipposito",
         is_verified=True
      )

   registered_user = authenticate(
      username=user.username,
      password="pipposito"
   )

   return {
      'username': registered_user.username,
      'email': registered_user.email,
      'tokens': registered_user.tokens()
   }