from django.db import models
from product.models import Product
#

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                help_text='Добавить Продукт', verbose_name='Продукт')
    quantity = models.IntegerField(null=False, verbose_name='Количество Товара')


    @property
    def product_name(self):
        return self.product.name

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name


