# Generated by Django 2.1.3 on 2018-11-25 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_auto_20181125_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9b009f0a-6463-4b9f-a22d-8eb96b716a72'), primary_key=True, serialize=False, unique=True),
        ),
    ]