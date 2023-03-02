from django_filters import rest_framework as filters

from .models import Product


class CharFiltersInFilters(filters.CharFilter, filters.BaseInFilter):
    pass

class ProductFilters(filters.FilterSet):
    category = filters.NumberFilter
    price = filters.RangeFilter()
    name = filters.CharFilter

    class Meta:
        model = Product
        fields = ['category', 'price', 'name']