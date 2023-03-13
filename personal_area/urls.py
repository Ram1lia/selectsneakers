from django.urls import path
from personal_area import views

get_post = {'get': 'list', 'post': 'create'}
get_put_delete = {'get': 'retrieve', 'put': 'update',
                  'delete': 'destroy'}

urlpatterns = [
    path('account/', views.AccountViewSet.as_view(get_post)),
    path('account/<int:id>/', views.AccountViewSet.as_view(get_put_delete)),
]