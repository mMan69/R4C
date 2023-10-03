from django.contrib import admin

from .models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ('serial', 'created')
    search_fields = ['serial']
    ordering = ['-created']


