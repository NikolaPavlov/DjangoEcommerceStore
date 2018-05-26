from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver

from webstore.models import Product

User = settings.AUTH_USER_MODEL

# Create your models here.

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            print('Cart exists!')
            is_new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            print('Create new cart!')
            cart_obj = Cart.objects.new(user=request.user)
            is_new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, is_new_obj


    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total_price = models.PositiveIntegerField(default=0)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def pre_save_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total_price = 0
        for product in products:
            total_price += product.price
        instance.total_price = total_price
        instance.save()

m2m_changed.connect(pre_save_cart_receiver, sender=Cart.products.through)
