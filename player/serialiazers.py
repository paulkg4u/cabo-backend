from rest_framework import  serializers
from django.db import transaction
from django.contrib.auth.models import User

from gameroom.models import Player


class PlayerSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(username=validated_data.pop('username'), email=validated_data.pop('email'),
                                     password=validated_data.pop('password'), **validated_data)
            new_player = Player.objects.create(user=user)
            return new_player

    class Meta:
        model = Player
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        exclude = ['password']


class PlayerModelSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Player
        fields = '__all__'





