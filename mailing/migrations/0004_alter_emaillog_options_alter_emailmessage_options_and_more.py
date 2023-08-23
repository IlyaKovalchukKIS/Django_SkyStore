# Generated by Django 4.2.3 on 2023-08-19 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_comment'),
        ('mailing', '0003_emaillog_emailmessage_emailsettings_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emaillog',
            options={'verbose_name': 'лог', 'verbose_name_plural': 'логи'},
        ),
        migrations.AlterModelOptions(
            name='emailmessage',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.RemoveField(
            model_name='emaillog',
            name='message',
        ),
        migrations.RemoveField(
            model_name='emailmessage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='emailmessage',
            name='sent',
        ),
        migrations.RemoveField(
            model_name='emailmessage',
            name='subject',
        ),
        migrations.AddField(
            model_name='emaillog',
            name='email_settings',
            field=models.ManyToManyField(to='mailing.emailsettings', verbose_name='рассылка'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='text',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='текст'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='кому'),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='ответ'),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='sent_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата отправки'),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='emailsettings',
            name='frequency',
            field=models.CharField(choices=[('1', 'Ежедневно'), ('7', 'Еженедельно'), ('30', 'Ежемесячно')], max_length=20, verbose_name='периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='emailsettings',
            name='sending_time',
            field=models.CharField(choices=[('8', 'утро'), ('12', 'день'), ('19', 'вечер')], max_length=20, verbose_name='время рассылки'),
        ),
        migrations.AlterField(
            model_name='emailsettings',
            name='status',
            field=models.CharField(choices=[('created', 'создана'), ('completed', 'завершена'), ('launched', 'запущена')], max_length=20, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='emailsettings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='пользователи'),
        ),
    ]