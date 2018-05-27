from django.urls import path

from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_home, name='cart_home_url'),
    path('update/', views.cart_update, name='cart_update_url'),
    path('delete/<int:cart_id>/<int:product_id>/',
         views.remove_from_cart,
         name='remove_from_cart_url'),
]
