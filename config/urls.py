from django.urls import re_path
from .views import contacts_view

urlpatterns = [
    re_path(r'.*', contacts_view),
]
