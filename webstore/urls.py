from django.urls import path

from . import views


urlpatterns = [
    path('', views.products, name='index_url'),

    path('products_by_name',
         views.products_by_name,
         name='products_by_name_url'),
    path('products_by_category/cat/<int:pk>/',
         views.products_by_category,
         name='products_by_category_url'),
    path('products_in_cat_by_name/cat/<int:pk>/',
         views.products_in_cat_by_name,
         name='products_in_cat_by_name_url'),

    path('product/<int:pk>/',
         views.ProductDetailView.as_view(),
         name='product_detail_url'),

]
