from django.db import models
from apivault import settings
from vault.models import API

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    api = models.ForeignKey(API, on_delete=models.CASCADE, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Set a uniqueness constraint for the user-api combinations
        unique_together = ('user', 'api')
        db_table = 'like'


class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    api = models.ForeignKey(API, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'api')
        db_table = 'bookmark'