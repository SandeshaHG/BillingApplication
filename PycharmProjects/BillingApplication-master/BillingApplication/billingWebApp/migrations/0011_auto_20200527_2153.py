# Generated by Django 3.0.6 on 2020-05-27 16:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billingWebApp', '0010_auto_20200527_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemName',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.CharField(default=datetime.datetime(2020, 5, 27, 16, 23, 7, 134418, tzinfo=utc), max_length=20),
        ),
    ]