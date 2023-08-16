from django.contrib import admin

from mailing.models import Frequency, Mailing, Status, Message


# Register your models here.

@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('frequency',)
    search_fields = ('frequency',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('date_mailing', 'frequency', 'status',)
    list_filter = ('date_mailing', 'frequency', 'status',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', )
