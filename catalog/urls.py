"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView
from config import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/view/<int:pk>', ProductDetailView.as_view(), name='product_view'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
