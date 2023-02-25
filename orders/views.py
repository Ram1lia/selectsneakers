from rest_framework import permissions, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders.models import Order, OrderItem, Payment, Product
from .serializers import OrderSerializers, OrderItemSerializer, PaymentSerializer, ProductSerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'



class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        # return Response(data={"order_create": serializer.data, "redirect": "http://127.0.0.1:8000/api/v1/create_order/payment/"})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]



class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = "id"



