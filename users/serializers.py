from rest_framework import serializers
from rest_framework.serializers import *
from users.models import User
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=4, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {"password": {'write_only': True}}

    # def validate_password(self, attrs):
    #     password_exists = User.objects.filter(password=attrs['password']).exists()
    #     if password_exists:
    #         return super().validate(attrs)
    #     return 'password already exists'
    #
    # def validate_username(self, attrs):
    #     try:
    #         username_exists = User.objects.get(username=attrs['username'])
    #         if username_exists:
    #             return 'username already exists'
    #     except TypeError:
    #         return super().validate(attrs)
    #
    # def validate_email(self, attrs):
    #     try:
    #         email_exists = User.objects.get(email=attrs['email'])
    #         if email_exists:
    #             return "email already exists"
    #     except:
    #         return super().validate(attrs)
    #
    #
    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = super().create(validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["token"]