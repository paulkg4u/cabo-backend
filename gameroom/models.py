from uuid import uuid4
import random

from django.db import models

from player.models import Player


# Create your models here.
class GameRoom(models.Model):

    def generate_room_number():
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(chars) for _ in range(8))

    uuid = models.UUIDField(default=uuid4, primary_key=True)
    room_number = models.CharField(default=generate_room_number, unique = True, max_length=10)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE,related_name="creator")
    winner = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name="winner")
    created_at = models.DateTimeField(auto_now_add=True)
    players = models.TextField(default="")
    node_url = models.CharField(default="", max_length =200)
    num_players = models.IntegerField(default=1)
    status = models.CharField(default = "not_started", max_length = 20)
    
