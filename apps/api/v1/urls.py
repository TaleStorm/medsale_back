from django.urls import include, path
from ..views import GetUserOrProductOrOrder

urlpatterns = [
    path(
        'getUPO/',
        GetUserOrProductOrOrder.as_view(),
        name='user_order_product_api'
    )
]
