from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from .models import Account
from rest_framework.serializers import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = 'id user avatar full_name email phone'.split()


class AccountValidateSerializer(serializers.Serializer):
    full_name = serializers.CharField(min_length=1, required=True)
    email = serializers.EmailField(required=True)
    phone = PhoneNumberField(required=True)
