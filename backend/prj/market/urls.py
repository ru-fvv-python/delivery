from django.urls import path
from market.views.auth import AuthView, hello
from market.views.product import ProductListView

urlpatterns = [
    path('produc_list', ProductListView.as_view()),
    path('userlogin/', AuthView.as_view()),
    path('hello/', hello)
]