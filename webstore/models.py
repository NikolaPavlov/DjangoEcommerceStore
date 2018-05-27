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
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ManyToManyField('Category')
    image = ImageField(upload_to='img/')

    def get_categories(self):
        # return "\n".join([c.name for c in self.category.all()])
        return ([c for c in self.category.all()])

    def __str__(self):
        return self.name
