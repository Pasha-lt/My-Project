from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from orders.views import orders_page, OrderView

router = SimpleRouter()

router.register('api/orders', OrderView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', orders_page),
]

urlpatterns += router.urls