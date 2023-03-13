from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework import status, viewsets, permissions
from .models import Product, Category
from .serializers import ProductListSerializer, ProductDetailListSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailListSerializer
    lookup_field = 'id'