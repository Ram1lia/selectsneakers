from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework import status, viewsets
from products.models import Product, Category
from products.serializers import ProductListSerializer, ProductDateilListSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
