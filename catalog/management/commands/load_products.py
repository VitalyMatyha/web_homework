from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'data.json')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
