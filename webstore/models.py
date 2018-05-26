from django.db import models
from django.conf import settings

from sorl.thumbnail import ImageField


from users.models import User

User = settings.AUTH_USER_MODEL

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)  # required True
    description = models.TextField()
    price = models.IntegerField()
    category = models.ManyToManyField('Category', blank=True)
    # image = models.ImageField(null=True, blank=True, upload_to='img/')
    image = ImageField(upload_to='img/')

    def __str__(self):
        return self.name
