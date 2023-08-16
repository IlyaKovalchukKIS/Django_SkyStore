from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Frequency(models.Model):
    frequency = models.CharField(max_length=50, verbose_name='период рассылки')

    def __str__(self):
        return self.frequency

    class Meta:
        verbose_name = 'период'
        verbose_name_plural = 'период'


class Status(models.Model):
    status = models.CharField(max_length=40, verbose_name='статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    text = models.TextField(max_length=500, verbose_name='письмо')

    def __str__(self):
        return f'{self.title} {self.text}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Mailing(models.Model):
    date_mailing = models.DateTimeField(auto_now_add=True, verbose_name='дата рассылки')
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE, verbose_name='период рассылки')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='статус')
    message = models.ForeignKey(Message, on_delete=models.DO_NOTHING, verbose_name='письмо', **NULLABLE)

    def __str__(self):
        return f'{self.date_mailing} {self.frequency}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
