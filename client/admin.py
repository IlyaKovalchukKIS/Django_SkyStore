from django.contrib import admin

from client.models import Client


# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'name', 'email', 'phone',)
    search_fields = ('login', 'name',)
    list_filter = ('login',)

