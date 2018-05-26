from django.db import models
from django.conf import settings

from webstore.models import User
from cart.models import Cart

User = settings.AUTH_USER_MODEL

# Create your models here.

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user addr
    # user name
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product) ---> products are in cart
    # bill = models.PositiveIntegerField(default=0) ---> this is in cart


    def __str__(self):
        return str(self.id)
