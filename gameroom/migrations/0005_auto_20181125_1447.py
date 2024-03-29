# Generated by Django 2.1.3 on 2018-11-25 14:47

from django.db import migrations, models
import gameroom.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gameroom', '0004_auto_20181125_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroom',
            name='room_number',
            field=models.IntegerField(default=gameroom.models.GameRoom.generate_room_number, unique=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e03d69f0-c8a1-4e03-8c04-d24e9aeacdd9'), primary_key=True, serialize=False, unique=True),
        ),
    ]
