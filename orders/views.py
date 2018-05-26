from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Order
from cart.models import Cart


# Create your views here.

@login_required()
def create_order(request):
    cart_obj, is_new_obj = Cart.objects.new_or_get(request)
    order_obj, is_new_order_obj = Order.objects.get_or_create(cart=cart_obj, user=request.user)
    return render(request, 'thank_you_for_order.html', {'order':order_obj})
