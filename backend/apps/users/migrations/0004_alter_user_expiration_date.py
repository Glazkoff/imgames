# Generated by Django 3.2.12 on 2023-03-29 14:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230329_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 14, 0, 13, 975039, tzinfo=utc), verbose_name='Дата окончания подписки'),
        ),
    ]
