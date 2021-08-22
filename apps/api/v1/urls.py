from django.urls import include, path
from ..views import GetUserOrProductOrOrder, OrderViewSet, ProductViewSet


urlpatterns = [
    path(
        'getUPO/',
        GetUserOrProductOrOrder.as_view(),
        name='user_order_product_api'
    ),
    path('orders', OrderViewSet.as_view({'get': 'list'}), name='orders'),
    path('products', ProductViewSet.as_view({'get': 'list'}), name='products')
]
