from django.db import models
from sneakersshop2 import settings
from users.models import User
from product.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                help_text='Добавить Продукт', verbose_name='Продукт')
    quantity = models.IntegerField(null=False, verbose_name='Количество Товара')

    def cart_items_list(self):
        return [{"id": item.id, "cart_id": item.cart.id, "product_id": item.product.id, "quantity": item.quantity} for
                item in self.items.all()]
    @property
    def product_name(self):
        return self.product.name

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

    def add_quantity(self, amount):
        self.quantity += amount
        self.save()
