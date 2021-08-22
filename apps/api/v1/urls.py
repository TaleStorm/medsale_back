from django.urls import include, path
from ..views import GetUserOrProductOrOrder, OrderViewSet

urlpatterns = [
    path(
        'getUPO/',
        GetUserOrProductOrOrder.as_view(),
        name='user_order_product_api'
    ),
    path('orders', OrderViewSet, name='orders_list')
]
