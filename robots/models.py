from django.db import models
from django.core.mail import send_mail

from R4C.settings import EMAIL_HOST_USER


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f'{self.serial}'

    def __repr__(self):
        return f'{self.serial}, {self.model}, {self.version}, {self.created}'

    def send_email(self, order):

        subject = 'Производство Роботов'

        message = (f'Добрый день!\n'
                   f'Недавно вы интересовались нашим роботом модели {self.model}, версии {self.version}.\n'
                   f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.')

        send_mail(subject, message, EMAIL_HOST_USER, [order.customer])

        order.is_notified = True
        order.save()
