# Generated by Django 4.2.3 on 2023-08-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_last_change',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения'),
        ),
    ]