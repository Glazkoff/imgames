# Generated by Django 3.2 on 2022-01-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_remove_month_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='money_per_month',
            field=models.PositiveIntegerField(default=100000, verbose_name='Бюджет на месяц'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='number_of_turns',
            field=models.PositiveIntegerField(verbose_name='Количество шагов'),
        ),
    ]
