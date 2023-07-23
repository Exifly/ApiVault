from apivault import settings
from django.db import models
from vault.models import API

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    api = models.ForeignKey(API, on_delete=models.CASCADE, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Set a uniqueness constraint for the user-api combinations
        unique_together = ('user', 'api')


    def __str__(self):
        return f"{self.user} - {self.api}"


class Feedback(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=150, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        username = "Anonymous" if self.name is None else self.name
        return f"{username} - {self.message}"
