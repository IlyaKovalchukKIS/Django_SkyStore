# Generated by Django 4.2.3 on 2023-08-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_comment'),
        ('mailing', '0006_remove_emailsettings_message_emailsettings_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailsettings',
            name='user',
        ),
        migrations.AddField(
            model_name='emailsettings',
            name='user',
            field=models.ManyToManyField(to='client.client', verbose_name='пользователи'),
        ),
    ]
