from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductViewSet.as_view({'get','list',})),
    path('products/<int:id>/', view.ProductViewSet.as_view({'get' : 'retrieve'}))
]
