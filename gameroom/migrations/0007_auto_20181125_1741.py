# Generated by Django 2.1.3 on 2018-11-25 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gameroom', '0006_auto_20181125_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='num_players',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a7e723ce-5d85-4fca-8d17-4502f0be79bf'), primary_key=True, serialize=False, unique=True),
        ),
    ]
