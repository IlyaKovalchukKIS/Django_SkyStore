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

from blog.apps import BlogConfig
from blog.views import BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView, BlogCreateView
from catalog.views import home, contacts
from config import settings
from django.conf.urls.static import static

app_name = BlogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/list/', BlogListView.as_view(), name='blog_list'),
    path('blog/view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
