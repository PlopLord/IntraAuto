# Generated by Django 3.0.4 on 2020-04-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='day',
            field=models.DateTimeField(),
        ),
    ]