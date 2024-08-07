# Generated by Django 5.0.7 on 2024-08-05 11:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_user_businessnumber_user_businessinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=10)),
                ('goal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PointHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('currentPoint', models.IntegerField(default=0)),
                ('increasePoint', models.IntegerField(blank=True, null=True)),
                ('decreasePoint', models.IntegerField(blank=True, null=True)),
                ('userFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
