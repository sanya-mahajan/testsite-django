# Generated by Django 3.2.12 on 2022-08-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateField(),
        ),
    ]
