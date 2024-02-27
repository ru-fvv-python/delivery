from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from market.models import Product, Category
from market.views.category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продукции (отвечает за входные и выходные данные)
    """
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category']


class ProductListView(GenericAPIView, ListModelMixin):
    """
        Список продукции
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
