from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from orders.views import orders_page, OrderView, orders_app

router = SimpleRouter()

router.register('api/orders', OrderView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', orders_page),
    path('orders_page/', orders_app),
]

urlpatterns += router.urls