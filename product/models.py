from colorfield import fields
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Бренды')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категории')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип')

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = fields.ColorField()
    size = models.PositiveSmallIntegerField(null=True, unique=True, verbose_name='Размер')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    season = models.IntegerField(null=True, choices=(
        (1, "winter"),
        (2, "summer"),
        (3, "fall_and_sping"),
    ))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
