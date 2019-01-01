from player.models import Player

def get_player_by_username(username):
    try:
        player = Player.objects.get(user__username = username)    
        return player
    except Player.DoesNotExist:
        return None


def get_player_by_uuid(uuid):
    try:
        player = Player.objects.get(uuid = uuid)    
        return player
    except Player.DoesNotExist:
        return None
        
    

