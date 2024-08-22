from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discription = models.TextField()
    specifications = models.JSONField(default=dict)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.quantity > 0 

    @property
    def is_new(self):
        return now() - timedelta(days=1) < self.created_at 

    class Meta:
        ordering = ["-created_at"]

    


class ProductImage(BaseModel):
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.product.name


class User(AbstractUser):
    class Type(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USERS = 'user', 'User'
        OPERATORS = 'operator', 'Operator'
        COURIERS = 'courier', 'Courier'
        MANAGERS = 'manager', 'Manager'

    type = models.CharField(max_length=255, choices=Type.choices, default=Type.USERS)
    image = models.ImageField(upload_to = 'user/', blank=True, null=True, default="assets/img/icons/weather-sm.jpg")
    about_me = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)

class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name
    