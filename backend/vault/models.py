from django.db import models
from apivault import settings

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
   source = models.CharField(max_length=100, default="")

   def __str__(self):
      return self.name
   
   @property
   def num_likes(self):
      # Compute the number of Likes associated with this API object
      return self.like_set.count()
