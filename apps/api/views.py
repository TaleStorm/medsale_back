from rest_framework import generics
from rest_framework.response import Response
from order.models import Order
from product.models import Product
from user.models import User
from order.srializers import OrderSerializer
from product.srializers import ProductSerializer
from user.srializers import UserSerializer
from django.shortcuts import get_object_or_404


class QueryToModelOrSerializer():
    data = {
        'product': [Product, ProductSerializer],
        'user': [User, UserSerializer],
        'order': [Order, OrderSerializer],
    }

    def get_model(self, model: str) -> object:
        return self.data[model][0]

    def get_serializer(self, model: str, *args, **kwargs) -> object:
        return self.data[model][1]


class GetUserOrProductOrOrder(generics.RetrieveAPIView):
    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.request.query_params.get('id', None)
        #lookup_user_id = self.request.query_params.get('user_id', None)

        filter_kwargs = {self.lookup_field: lookup_url_kwarg}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj

    def get_queryset(self):
        model = self.request.query_params.get('model')
        return QueryToModelOrSerializer().get_model(model)

    def get_serializer_class(self):
        model = self.request.query_params.get('model')
        return QueryToModelOrSerializer().get_serializer(model)
