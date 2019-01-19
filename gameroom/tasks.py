from django.conf import settings
import random

from firebase import firebase
from gameroom import utils as game_room_utils
from player import utils as player_utils
from constants import CARD_CODES, PLAYER_STATUS, CARD_VALUES
from helpers import shuffle_cards
from player.serialiazers import PlayerModelSerializer

firebase_application = firebase.FirebaseApplication(settings.FIREBASE_URL)

def create_game_room_node(game_room_uuid):
    game_room = game_room_utils.get_game_room_by_uuid(game_room_uuid)
    player_data = PlayerModelSerializer(game_room.owner).data
    game_room_data = dict(
        id = game_room.room_number,
        uuid = str(game_room.uuid),
        events = [],
        played_cards = ['XX'],
        cards_on_deck = shuffle_cards(CARD_CODES),
        player_order = [str(game_room.owner.uuid)],
        player_status = {
            str(game_room.owner.uuid) : PLAYER_STATUS
        },
        player_info = {
            str(game_room.owner.uuid) :  player_data
        },
        game_status = 'not_started'
    )
    game_room_node = firebase_application.post('/gamerooms/',game_room_data)
    game_room_address = str(game_room_node['name'])
    game_room.node_url = game_room_address
    game_room.save()

def add_player_to_room(node_address, player_uuid):
    player = player_utils.get_player_by_uuid(player_uuid)
    serializer = PlayerModelSerializer(player).data
    firebase_node = firebase_application.get('/gamerooms/'+node_address, None)
    firebase_node['player_order'].append(str(player.uuid))
    firebase_application.put('/gamerooms/'+node_address, 'player_order', firebase_node['player_order'])
    firebase_application.put('/gamerooms/'+node_address+'/player_info', str(player.uuid), serializer)
    firebase_application.put('/gamerooms/'+node_address+'/player_status', str(player.uuid), PLAYER_STATUS)
    

def start_game(node_address):
    firebase_node = firebase_application.get('/gamerooms/'+node_address, None)
    firebase_application.put('/gamerooms/'+node_address, 'game_status', 'waiting_for_ready')
    cards = shuffle_cards(CARD_CODES)
    for each_player in firebase_node['player_order']:
        cards_for_player = random.sample(cards, 4)
        for each_card in cards_for_player:
            cards.remove(each_card)
        firebase_application.put('/gamerooms/'+node_address+'/player_status/'+each_player, 'cards', cards_for_player)
    
    firebase_application.put('/gamerooms/'+node_address, 'cards_on_deck', cards)
    firebase_application.put('/gamerooms/'+node_address,'current_player', firebase_node['player_order'][0])


def find_winner(node_address, room_uuid):
    game_room = game_room_utils.get_game_room_by_uuid(room_uuid)
    player_status = firebase_application.get('/gamerooms/'+node_address, 'player_status')
    player_info = firebase_application.get('/gamerooms/'+node_address, 'player_info')
    player_points = dict()
    winner_points = 1000
    winner = ""
    for each_player in player_status:
        points = 0
        for each_card in player_status[each_player].get('cards'):
            points+=CARD_VALUES[each_card]
        player_status[each_player]['points'] = points
        player_info[each_player]['points'] = points
        player_points[each_player] = points
        
        if points<winner_points:
            winner = each_player
            winner_points = points
        
    winner = player_utils.get_player_by_uuid(winner)
    game_room.winner = winner
    game_room.save()
    firebase_application.put('/gamerooms/'+node_address, 'player_status', player_status)
    firebase_application.put('/gamerooms/'+node_address, 'game_status', 'completed')
    firebase_application.put('/gamerooms/'+node_address, 'player_info', player_info)

    