# Generated by Django 3.0.4 on 2020-04-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0003_auto_20200417_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='day',
            field=models.DateTimeField(),
        ),
    ]