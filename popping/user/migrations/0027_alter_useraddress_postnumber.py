# Generated by Django 5.0.7 on 2024-08-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0026_alter_useraddress_phonenumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useraddress",
            name="postNumber",
            field=models.CharField(max_length=6),
        ),
    ]
