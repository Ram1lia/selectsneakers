from rest_framework import generics
from .models import *

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

from .filters import ProductFilters
from django_filters.rest_framework import DjangoFilterBackend


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProductFilters


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

