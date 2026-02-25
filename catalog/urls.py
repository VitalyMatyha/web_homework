from django.urls import path
from .views import home, contacts
from .views import index, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]