# Generated by Django 5.0.1 on 2024-01-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_interestpoint_address_interestpoint_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campernightpoint',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='interestpoint',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]