from django.shortcuts import render

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from market.models import Category

"""
    Generic-сериализаторы
"""

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Сериализатор для Категорий (отвечает за входные и выходные данные)
    """

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryViewSet(viewsets.ModelViewSet):
    """
        Конечные точки API,
        которые позволяют пользователям читать и изменять категории.
    """
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']

    @action(methods=['post'], detail=False,)
    def set_password(self, request, ):
        """Пример своих методов"""
        pass
