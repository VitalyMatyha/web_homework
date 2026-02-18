from django.urls import path, include  # подключаем include

urlpatterns = [
    path('', include('catalog.urls')),  # все маршруты из catalog
]
