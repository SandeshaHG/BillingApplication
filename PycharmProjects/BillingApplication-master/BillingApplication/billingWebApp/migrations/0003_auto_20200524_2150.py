# Generated by Django 3.0.6 on 2020-05-24 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billingWebApp', '0002_order_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.CharField(default=datetime.datetime(2020, 5, 24, 16, 20, 21, 109265, tzinfo=utc), max_length=20),
        ),
    ]
