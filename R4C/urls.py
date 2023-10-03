from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('robots.urls', namespace='robots')),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders'))
]
