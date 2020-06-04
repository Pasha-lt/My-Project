from django.contrib import admin
from django.urls import path

from orders.views import orders_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', orders_page),
]
