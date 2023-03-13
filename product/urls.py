from django.urls import path
from . import views

get_post = {'get': 'list', 'post': 'create'}
get_put_delete = {'get': 'retrieve', 'put': 'update',
                  'delete': 'destroy'}

urlpatterns = [
    path('', views.ProductViewSet.as_view(get_post)),
    path('<int:id>/', views.ProductDetailViewSet.as_view(get_put_delete))
]
