# Generated by Django 5.0.7 on 2024-08-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("popup", "0006_rename_productlike_product_view"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="discription",
        ),
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
