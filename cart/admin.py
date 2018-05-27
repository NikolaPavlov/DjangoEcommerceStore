from django.contrib import admin

from .models import Cart

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_products', 'total_price')


admin.site.register(Cart, CartAdmin)
