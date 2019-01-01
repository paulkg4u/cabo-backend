from firebase import firebase

from gameroom.models import GameRoom
from player import utils as player_utils
from gameroom import tasks as game_room_tasks
from gameroom import serializers as game_room_serializers

def create_game_room(req_obj):
    player = player_utils.get_player_by_username(req_obj.username)
    new_game_room = GameRoom.objects.create(owner = player, players = str(player.uuid))
    req_obj.game_room_uuid = new_game_room.uuid
    game_room_tasks.create_game_room_node(str(req_obj.game_room_uuid))
    serializer = game_room_serializers.GameRoomSerializer(new_game_room)
    return serializer.data


def join_game_room(req_obj):
    # todo : check number of players in gameroom
    player = player_utils.get_player_by_username(req_obj.username)
    game_room = GameRoom.objects.get(room_number = req_obj.game_room_id)

    if (str(player.uuid) not in game_room.players) and (game_room.status == 'not_started'):
        game_room.players = game_room.players+','+str(player.uuid)
        game_room.num_players+=1
        game_room.save()
        game_room_tasks.add_player_to_room(str(game_room.node_url),str(player.uuid))
    elif game_room.status != 'not_started' and str(player.uuid) not in game_room.players:
        return {'success':False, 'error':'game_started'}
    serializer  = game_room_serializers.GameRoomSerializer(game_room)
    return serializer.data

def start_game(req_obj):
    player = player_utils.get_player_by_username(req_obj.username)
    print(req_obj.game_room_id)
    game_room = GameRoom.objects.get(room_number = req_obj.game_room_id)
    game_room.status = "started"
    game_room.save()
    game_room_tasks.start_game(str(game_room.node_url))
    return {'success':True}

def find_winner(req_obj):
    game_room =  GameRoom.objects.get(room_number = req_obj.game_room_id)
    game_room.status = "ended"
    game_room.save()
    game_room_tasks.find_winner(str(game_room.node_url), str(game_room.uuid))
    return {'success':True}




