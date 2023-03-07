from django.db import models
import uuid
from colorfield import fields


class BaseModel(models.Model):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name

    class Meta:
        abstract = True

class Brand(BaseModel):
    pass


class Category(BaseModel):
    pass


class Type(BaseModel):
    pass


class Product(Brand):
    image = models.ImageField(null=True, blank=True)
    article = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    text = models.TextField()
    color = fields.ColorField()
    size = models.PositiveSmallIntegerField()
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='products')
    season = models.IntegerField(choices=(
        (1, "winter"),
        (2, "summer"),
        (3, "fall_and_sping"),
    ))
