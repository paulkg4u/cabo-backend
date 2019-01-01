from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    uuid = models.UUIDField(default=uuid4(), unique=True, primary_key=True)
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pic_url =  models.URLField(default = "")

