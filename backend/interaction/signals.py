from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like

@receiver(post_save, sender=Like)
def increment_likes_count(sender, instance, created, **kwargs):
    if created:
        instance.api.likes_count += 1
        instance.api.save()

@receiver(post_delete, sender=Like)
def decrement_likes_count(sender, instance, **kwargs):
    instance.api.likes_count -= 1
    instance.api.save()
