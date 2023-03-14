from django.urls import path
from . import views

get_post = {'get': 'list', 'post': 'create'}
get_put_delete = {'get': 'retrieve', 'put': 'update',
                  'delete': 'destroy'}

urlpatterns = [
    path('cart/', views.CartViewSet.as_view(get_post)),
    path('cart/<int:id>/', views.CartViewSet.as_view(get_put_delete))
]
