# Generated by Django 3.2.12 on 2023-02-13 18:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0014_alter_stageofchannel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='conversion',
            field=models.DecimalField(decimal_places=4, max_digits=5, validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.01)], verbose_name='Стандартная конверсия на этапе'),
        ),
    ]