from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Cart
from .serializers import CartSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['product', 'quantity']
    lookup_field = 'id'
