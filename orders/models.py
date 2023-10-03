from django.db import models

from customers.models import Customer
from robots.models import Robot


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
    is_pending = models.BooleanField(default=False)  # флаг ожидания заказа
    is_notified = models.BooleanField(default=False)  # флаг отправки уведомления о производстве робота

    def __str__(self):
        return f'{self.robot_serial}'

    def is_exist_robot(self):
        return Robot.objects.filter(serial=self.robot_serial).exists()
