from django.contrib import admin

from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    # readonly_fields = ["created_at"]
    date_hierarchy = 'created_at'
    fields = ('user', 'cart')
    list_display = ('created_at',
                    'get_user_name',
                    'get_shipping_addr',
                    'get_order_products',
                    'get_total_price',
                    'products_num')


    def get_user_name(self, obj):
        return obj.user.username

    def get_shipping_addr(self, obj):
        return obj.user.shipping_addr

    def get_order_products(self, obj):
        products_in_the_order = obj.cart.products.all()
        return ', '.join(p.name for p in products_in_the_order)

    def get_total_price(self, obj):
        return obj.cart.total_price

    def products_num(self, obj):
        return obj.cart.products.all().count()

admin.site.register(Order, OrderAdmin)
