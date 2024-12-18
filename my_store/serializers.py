from rest_framework import serializers

from my_store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id', 'name', 'description',
                 'price', 'image']
