# Generated by Django 2.1.3 on 2018-11-25 14:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_auto_20181125_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c143a78e-308b-4752-afd2-eb6f284eaf5d'), primary_key=True, serialize=False, unique=True),
        ),
    ]
