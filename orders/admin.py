from django.contrib import admin

from .models import Order


@admin.register(Order)
class RobotAdmin(admin.ModelAdmin):
    list_display = ('customer', 'robot_serial')

