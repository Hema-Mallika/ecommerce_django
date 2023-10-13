# Generated by Django 3.0.6 on 2020-05-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]