from . import views
from .views import home, contacts
from .views import index, product_detail
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductsByCategoryView,
    ProductDeleteView
)
from django.urls import path, include


urlpatterns = [
    path('', include('catalog.urls')),
]


urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]


urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', views.unpublish_product, name='unpublish_product'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]

