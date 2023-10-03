from django.contrib import admin
from django.urls import path

from . import views

app_name = 'robots'

urlpatterns = [
    path('create', views.create_robot, name='create_robot'),
    path('download', views.download_report, name='download_report')
]
