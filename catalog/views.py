from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product

# Главная страница
class IndexView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'


# Страница одного товара
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# Страница контактов
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def index(request):
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {'products': products})
