from django.urls import path

from . import views

app_name = 'robots'

urlpatterns = [
    path('', views.index, name='index'),
    path('robots/create', views.create_robot, name='create_robot'),
    path('robots/download', views.download_report, name='download_report')
]

