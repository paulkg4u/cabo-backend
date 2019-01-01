from gameroom.models  import GameRoom


def get_game_room_by_uuid(uuid):
    try:
        game_room = GameRoom.objects.get(uuid = uuid)
        return game_room
    except GameRoom.DoesNotExist:
        return None


def get_game_room_by_id(id):
    try:
        game_room = GameRoom.objects.get(id = id)
        return game_room
    except GameRoom.DoesNotExist:
        return None