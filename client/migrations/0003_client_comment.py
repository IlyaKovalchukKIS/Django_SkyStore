# Generated by Django 4.2.3 on 2023-08-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_options_alter_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='комментарий'),
        ),
    ]