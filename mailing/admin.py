from django.contrib import admin

from mailing.models import EmailMessage, EmailSettings, EmailLog


# Register your models here.

@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',)
    search_fields = ('id', 'title',)


@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sending_time', 'frequency', 'status', 'message',)
    list_filter = ('user', 'sending_time', 'status',)


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'sent_datetime', 'status', 'response',)

