# Generated by Django 5.0.1 on 2024-01-21 15:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_alter_categories_id_alter_imageinterestpoint_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='imageinterestpoint',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='interestpoint',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
