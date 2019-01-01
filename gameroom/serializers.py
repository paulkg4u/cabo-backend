from rest_framework.serializers import ModelSerializer

from gameroom.models import GameRoom


class GameRoomSerializer(ModelSerializer):

    class Meta:
        model = GameRoom
        fields = '__all__'


