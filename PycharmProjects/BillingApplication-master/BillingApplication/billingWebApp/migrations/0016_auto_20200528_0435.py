# Generated by Django 3.0.6 on 2020-05-27 23:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billingWebApp', '0015_auto_20200528_0336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='categoryId',
            new_name='category',
        ),
        migrations.AddField(
            model_name='payment',
            name='totalDue',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='payment',
            name='totalPaid',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='gstslab',
            name='slabPercentage',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.CharField(default=datetime.datetime(2020, 5, 27, 23, 5, 8, 698242, tzinfo=utc), max_length=20),
        ),
    ]
