from django.db import models


CATEGORY = (
    ('Man','мужской'),
    ('Woman','Женский'),
    ('Kids', 'Детские')

)
#ттт

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100,choices=CATEGORY)



    def __str__(self):
        return self.name





