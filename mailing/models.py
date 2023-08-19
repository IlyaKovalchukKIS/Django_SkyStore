from django.db import models

from client.models import Client

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class EmailMessage(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок', **NULLABLE)
    text = models.TextField(max_length=1000, verbose_name='текст', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class EmailSettings(models.Model):
    FREQUENCY_CHOICES = [
        ('1', 'Ежедневно'),
        ('7', 'Еженедельно'),
        ('30', 'Ежемесячно'),
    ]

    SENDING_TIME_CHOICES = [
        ('8', 'утро'),
        ('12', 'день'),
        ('19', 'вечер')
    ]

    STATUS_CHOICES = [
        ('created', 'создана'),
        ('completed', 'завершена'),
        ('launched', 'запущена')
    ]
    user = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='пользователи')
    sending_time = models.CharField(max_length=20, choices=SENDING_TIME_CHOICES, verbose_name='время рассылки')
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, verbose_name='периодичность рассылки')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='статус')
    message = models.ForeignKey(EmailMessage, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.user.email} - {self.frequency}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class EmailLog(models.Model):
    recipient = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='кому')
    sent_datetime = models.DateTimeField(verbose_name='дата отправки', **NULLABLE)
    status = models.CharField(max_length=50, **NULLABLE, verbose_name='статус')
    response = models.TextField(**NULLABLE, verbose_name='ответ')
    email_settings = models.ManyToManyField(EmailSettings, verbose_name='рассылка')

    def __str__(self):
        return f'{self.recipient} {self.sent_datetime} {self.status} {self.email_settings}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
