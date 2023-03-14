import re
from rest_framework import serializers
from orders.models import Order, OrderItem, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "id card_number date cvc_code name".split()

    def validate_card_number(self, value):
        if len(value) != 16 or not value.isdigit():
            raise serializers.ValidationError("Номер карты должен содержать 16 цифр!")
        return value

    def validate_cvc_code(self, value):
        if len(value) != 3 or not value.isdigit():
            raise serializers.ValidationError("CVC код должен содержать 3 цифр!")
        return value


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "id user first_name last_name phone_number city street_name zip_code house status".split()

        def create(self, validate_data):
            return Order.objects.create(**validate_data)

    def validate_email(self, email):
        """
        Ensure email is valid.
        """
        if not email:
            raise serializers.ValidationError("Электронная почта обязательна!")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise serializers.ValidationError("Электронная почта недействительна!")
        return email

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Номер телефона должен содержать только цифры.')
        return value

    def validate_zip_code(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("Индекс должен состоять из 6 цифр")
        return value

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('Имя должно содержать только буквы.')
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('Фамилия должна содержать только буквы.')
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()
    cost = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = "id order_id product quantity cost".split()

    def get_cost(self, cost):
        return cost.get_cost()

    def create(self, validated_data):
        order_id = validated_data.pop('order_id')
        order = Order.objects.get(id=order_id)
        order_item = OrderItem.objects.create(order=order, **validated_data)
        return order_item
