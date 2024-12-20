# Generated by Django 5.1.3 on 2024-11-20 02:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_customer_mobile_number_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=128, validators=[django.core.validators.MinLengthValidator(3, message='Debe tener por lo menos 3 caracteres')], verbose_name='dirección'),
            preserve_default=False,
        ),
    ]
