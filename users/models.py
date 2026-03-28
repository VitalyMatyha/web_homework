from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None  # убираем username

    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    phone = models.CharField(max_length=35, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email