# Generated by Django 3.2.12 on 2022-12-27 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0025_round_is_old'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='is_old',
        ),
    ]