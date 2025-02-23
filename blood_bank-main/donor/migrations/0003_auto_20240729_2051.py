# Generated by Django 3.0.5 on 2024-07-29 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20210213_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')]),
        ),
    ]
