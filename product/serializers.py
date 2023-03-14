from rest_framework import serializers
from .models import Product, Category
from colorfield.serializers import ColorField
import uuid


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"