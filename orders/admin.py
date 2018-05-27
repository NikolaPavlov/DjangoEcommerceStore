from django.contrib import admin

from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    fields = ('created_at', 'user', 'shipping_addr', 'cart', 'total_price')
    list_display = ('id',
                    'created_at',
                    'user_name',
                    'shipping_addr',
                    'order_products',
                    'total_price',
                    'products_num')
    readonly_fields = ('created_at', 'shipping_addr', 'total_price')
    list_filter = ('cart__user',)
    search_fields = ['user__username']

    def user_name(self, obj):
        return obj.user.username

    def shipping_addr(self, obj):
        return obj.user.shipping_addr

    def order_products(self, obj):
        products_in_the_order = obj.cart.get_products()
        return products_in_the_order

    def total_price(self, obj):
        return obj.cart.total_price

    def products_num(self, obj):
        return obj.cart.products.all().count()

    def test(self, obj):
        return obj.user.username


admin.site.register(Order, OrderAdmin)
