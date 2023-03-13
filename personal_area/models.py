from django.db import models
from django.core.validators import FileExtensionValidator
from django.template.context_processors import media
from phonenumber_field.modelfields import PhoneNumberField
from sneakersshop2 import settings

class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = PhoneNumberField(unique=True)
    avatar = models.ImageField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


