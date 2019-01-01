# Generated by Django 2.1.3 on 2018-11-26 20:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0008_auto_20181126_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ed59fe26-5d84-432e-8a21-5e1542d57513'), primary_key=True, serialize=False, unique=True),
        ),
    ]