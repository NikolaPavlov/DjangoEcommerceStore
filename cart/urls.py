from django.urls import path, re_path

from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_home, name='cart_home_url'),
    path('update/', views.cart_update, name='cart_update_url'),
]
