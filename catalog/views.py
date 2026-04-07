from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .services import get_products_by_category
from django.core.cache import cache
from django.conf import settings



class ProductsByCategoryView(ListView):
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return get_products_by_category(category_id)


@method_decorator(cache_page(60 * 5), name='dispatch')  # 5 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if not request.user.has_perm('catalog.can_unpublish_product'):
        raise PermissionDenied

    product.is_published = False
    product.save()

    return redirect('catalog:product_detail', pk=pk)

# Главная страница
class IndexView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'


# Страница одного товара
class ProductDetailView(LoginRequiredMixin, DetailView):
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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        # если кеш выключен — просто возвращаем из БД
        if not settings.CACHE_ENABLED:
            return Product.objects.all()

        key = 'product_list'
        products = cache.get(key)

        # если в кеше нет — берём из БД и кладём в кеш
        if products is None:
            products = Product.objects.all()
            cache.set(key, products, 60 * 5)  # 5 минут

        return products

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.object.pk])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.owner != request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)