# Generated by Django 4.1.3 on 2023-02-08 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2023, 2, 13)),
        ),
    ]
