from django.urls import path
from .views import *
create_list = {'get': 'list', 'post': 'post'}

urlpatterns = [
    path('login/', LoginViewSet.as_view(create_list), name="login"),
    path('register/', RegisterViewSet.as_view(create_list), name='signup')
]