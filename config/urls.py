from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # подключаем include

urlpatterns = [
    path('', include('catalog.urls')),  # все маршруты из catalog
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
