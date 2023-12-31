from datetime import datetime

from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings as email_name
from client.models import Client
from mailing.models import EmailSettings, EmailLog


def send_email():
    current_time = timezone.now().time().hour
    settings = EmailSettings.objects.filter(status='created', sending_time=current_time).prefetch_related('user')
    # for setting in settings:
    #     recipients = setting.user.all()
    #     email_message = setting.message
    #
    #     for user in recipients:
    #         last_sand = EmailLog.objects.filter(recipient=user.id)
    #         print(user.id, last_sand)

    for setting in settings:
        recipients = setting.user.all()
        email_message = setting.message

        for recipient in recipients:
            try:
                send_mail(
                    email_message.title,
                    email_message.text,
                    email_name.EMAIL_HOST_USER,
                    [recipient.email],
                    fail_silently=False,
                )
                status = 'Отправлено'
                response = ''
            except Exception as e:
                status = 'Ошибка'
                response = str(e)

            log = EmailLog.objects.create(
                recipient=recipient,
                sent_datetime=timezone.now(),
                status=status,
                response=response,
                email_settings=setting
            )
            log.save()
