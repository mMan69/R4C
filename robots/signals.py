from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Robot
from orders.models import Order


@receiver(post_save, sender=Robot)
def robot_created_notification(sender, instance, created, **kwargs):

    order = Order.objects.filter(
            robot_serial=instance.serial,
            is_notified=False,
            is_pending=True
        ).first()

    if created and order:
        instance.send_email(order)
