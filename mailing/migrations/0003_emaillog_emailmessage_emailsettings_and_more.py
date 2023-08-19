# Generated by Django 4.2.3 on 2023-08-16 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_comment'),
        ('mailing', '0002_message_mailing_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('response', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_time', models.TimeField()),
                ('frequency', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=20)),
                ('status', models.CharField(default='created', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='message',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='status',
        ),
        migrations.DeleteModel(
            name='Frequency',
        ),
        migrations.DeleteModel(
            name='Mailing',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='emaillog',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.emailmessage'),
        ),
        migrations.AddField(
            model_name='emaillog',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]
