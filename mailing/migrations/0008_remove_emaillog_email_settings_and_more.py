# Generated by Django 4.2.3 on 2023-08-19 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_remove_emailsettings_user_emailsettings_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emaillog',
            name='email_settings',
        ),
        migrations.AddField(
            model_name='emaillog',
            name='email_settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.emailsettings', verbose_name='рассылка'),
        ),
    ]
