# Generated by Django 2.1.3 on 2018-11-26 20:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gameroom', '0009_auto_20181126_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroom',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
