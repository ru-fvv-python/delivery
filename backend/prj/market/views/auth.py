from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

"""
    Это свои сериализаторы (не на основе модели)
"""

class CommonResponseSerializer(serializers.Serializer):
    """
        Сериализатор для возврата сообщений
    """
    status = serializers.IntegerField()
    message = serializers.CharField()


class LoginRequestSerialaizer(serializers.Serializer):
    """
        Сериализатор для приема логина и пароля
    """
    username = serializers.CharField()
    password = serializers.CharField()


class AuthView(APIView):
    """
        User login
    """

    @swagger_auto_schema(
        request_body=LoginRequestSerialaizer,
        responses={200: CommonResponseSerializer}
    )
    def post(self, request):
        return Response(CommonResponseSerializer({
            'status': 0,
            'message': 'OK'
        }).data)

@api_view()
def hello(request):
    return Response({
        'message':'Hello!'
    })