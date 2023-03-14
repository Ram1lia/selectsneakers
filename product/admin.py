from django.contrib import admin
from product.models import Product, Brand, Category, Type

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Type)
