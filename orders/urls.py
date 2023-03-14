from django.urls import path
from orders import views


get_post = {'get': 'list',
            'post': 'create'}
get_put_delete = {'get': 'retrieve',
                  'put': 'update',
                  'delete': 'destroy'}
urlpatterns = [
    path('payment/', views.PaymentViewSet.as_view(get_post)),
    path('payment/<int:id>/', views.PaymentViewSet.as_view(get_put_delete)),
    path('create_order/', views.OrderViewSet.as_view(get_post)),
    path('create_order/<int:id>/', views.OrderViewSet.as_view(get_put_delete)),
    path('order_item/', views.OrderItemViewSet.as_view(get_post)),
    path('order_item/<int:id>/', views.OrderItemViewSet.as_view(get_put_delete)),
]




