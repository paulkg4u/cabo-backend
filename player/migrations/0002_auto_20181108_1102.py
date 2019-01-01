# Generated by Django 2.1.3 on 2018-11-08 11:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('db5dadd9-61b3-4a94-a64f-2dff51f82275'), primary_key=True, serialize=False, unique=True),
        ),
    ]
