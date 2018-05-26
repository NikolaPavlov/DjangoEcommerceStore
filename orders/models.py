from django.db import models
from django.conf import settings

from webstore.models import User
from cart.models import Cart

User = settings.AUTH_USER_MODEL

# Create your models here.

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)
