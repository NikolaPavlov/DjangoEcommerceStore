from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.products, name='index_url'),
    re_path(r'^products_by_category/cat/(?P<pk>[0-9]+)/$',
        views.products_by_category, name='products_by_category_url'),
]
