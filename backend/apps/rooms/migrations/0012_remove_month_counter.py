# Generated by Django 3.2 on 2022-01-06 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_auto_20220106_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='month',
            name='counter',
        ),
    ]
