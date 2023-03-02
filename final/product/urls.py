from django.urls import path

from .views import ProductView, ProductDetail

urlpatterns = [
    path('api/sneakers/', ProductView.as_view()),
    path('api/sneakers/<int:pk>/', ProductDetail.as_view())
]