# Generated by Django 3.0.6 on 2020-05-27 16:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billingWebApp', '0007_auto_20200527_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.CharField(default=datetime.datetime(2020, 5, 27, 16, 6, 58, 169651, tzinfo=utc), max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='orderDate',
            field=models.CharField(default=datetime.datetime(2020, 5, 27, 16, 6, 58, 169651, tzinfo=utc), max_length=20),
        ),
    ]
