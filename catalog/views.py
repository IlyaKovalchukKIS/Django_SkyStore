from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from catalog.models import Product, Category
from catalog.forms import ProductForm


# Create your views here.

def home(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Топ товаров'
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'catalog/contacts.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price', 'date_creation', 'date_last_change',)
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        image = self.request.FILES.get('image')
        if image:
            new_product = form.save(commit=False)
            new_product.image = image
            new_product.save()
        else:
            form.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price', 'date_last_change',)
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
