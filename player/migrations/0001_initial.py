# Generated by Django 2.1.3 on 2018-11-07 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('6c0586de-8fc7-4b18-a8dd-fdf2dcd3355b'), primary_key=True, serialize=False, unique=True)),
                ('points', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]