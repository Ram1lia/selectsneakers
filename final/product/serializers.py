from rest_framework import serializers
from products.models import Product, Category
from colorfield.serializers import ColorField
import uuid


class ProductListSerializer(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField()
    color = ColorField()
    size = serializers.IntegerField()
    price = serializers.FloatField()


class ProductDateilListSerializer(ProductListSerializer):
    text = serializers.CharField()
    article = serializers.UUIDField()
