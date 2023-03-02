from django.db import models


CATEGORY = (
    ('Man','мужской'),
    ('Woman','Женский'),
    ('Kids', 'Детские')

)

COLOR = (
    ('ЧЕРНЫЙ ','ЧЕРНЫЙ'),
    ('ЖЕЛТЫЙ','ЖЕЛТЫЙ'),
    ('БЕЛЫЙ', 'БЕЛЫЙ'),
    ('ХАКИ', 'ХАКИ'),
    ('СЕРЫЙ', 'СЕРЫЙ'),


)
#ттт

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100,choices=CATEGORY)
    color = models.CharField(max_length=100,choices=COLOR)


    def __str__(self):
        return self.name
