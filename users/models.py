from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    shipping_addr= models.CharField(max_length=255)
