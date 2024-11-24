from django.db import models

from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField(blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)


    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be greater than zero")

    def __str__(self):
        return self.name