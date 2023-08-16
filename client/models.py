from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    login = models.CharField(max_length=100, verbose_name='логин', unique=True)
    password = models.CharField(max_length=20, verbose_name='пароль')

    name = models.CharField(max_length=150, verbose_name='имя', **NULLABLE)
    email = models.EmailField(max_length=150, verbose_name='почта', unique=True)
    phone = models.IntegerField(verbose_name='телефон', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} ( логин: {self.login} email: {self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

