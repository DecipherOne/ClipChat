# Generated by Django 2.1.5 on 2019-02-14 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_data', '0002_auto_20190214_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_time_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='date_time_edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
