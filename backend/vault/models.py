from django.db import models
from authentication.models import DefaultUser
class Category(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name
   
   class Meta:
      db_table = 'category'


class API(models.Model):
   AUTH_CHOICES = [
      ('apiKey', 'apiKey'),
      ('OAuth', 'OAuth'),
      ('', 'None'),
   ]

   name = models.CharField(max_length=100, db_index=True)
   auth = models.CharField(max_length=100, choices=AUTH_CHOICES)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   cors = models.BooleanField()
   description = models.TextField()
   https = models.BooleanField()
   url = models.URLField()
   
   view_count = models.PositiveIntegerField(default=0)
   owner = models.ForeignKey(DefaultUser, db_index=True, blank=True, null=True, on_delete=models.CASCADE)
   likes_count = models.PositiveIntegerField(default=0)


   def __str__(self):
      return self.name
   
class APIPending(models.Model):
   AUTH_CHOICES = [
      ('apiKey', 'apiKey'),
      ('OAuth', 'OAuth'),
      ('', 'None'),
   ]

   name = models.CharField(max_length=100, db_index=True)
   auth = models.CharField(max_length=100, choices=AUTH_CHOICES)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   cors = models.BooleanField()
   description = models.TextField()
   https = models.BooleanField()
   url = models.URLField()
   
   owner = models.ForeignKey(DefaultUser, db_index=True, blank=True, null=True, on_delete=models.CASCADE)


   def __str__(self):
      return self.name
   
