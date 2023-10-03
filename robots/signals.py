from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Robot


@receiver(post_save, sender=Robot)
def robot_created_notification(sender, instance, created, **kwargs):
    if created:
        instance.send_email()
