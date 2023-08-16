# Generated by Django 4.2.3 on 2023-08-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, unique=True, verbose_name='логин')),
                ('password', models.CharField(max_length=20, verbose_name='пароль')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='почта')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='телефон')),
            ],
        ),
    ]
