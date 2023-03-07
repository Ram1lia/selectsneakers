from django.contrib import admin
from products.models import Product, Brand, Type, Category

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Category)
