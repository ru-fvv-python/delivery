from django.urls import path
from market.views.auth import AuthView, hello

urlpatterns = [
    path('userlogin/', AuthView.as_view()),
    path('hello/', hello)
]