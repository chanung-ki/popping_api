# Generated by Django 5.0.7 on 2024-08-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("popup", "0003_order_buydate_order_currency_order_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="brands",
            name="follower",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="saved",
            field=models.IntegerField(default=0),
        ),
    ]
