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
from catalog.views import home, contacts, category_product, categories, create_product
from config import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/category_product/', category_product, name='category_product'),
    path('create_product/', create_product, name='create_product')
]
