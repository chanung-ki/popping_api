# Generated by Django 5.0.7 on 2024-08-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("popup", "0002_remove_brands_followers"),
        ("user", "0012_user_followed"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="saved_product",
            field=models.ManyToManyField(
                related_name="saving_product", to="popup.product"
            ),
        ),
    ]
