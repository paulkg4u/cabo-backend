# Generated by Django 2.1.3 on 2018-11-30 20:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0010_auto_20181126_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('379709c0-dfde-4880-985d-f332cb1c5b8b'), primary_key=True, serialize=False, unique=True),
        ),
    ]
