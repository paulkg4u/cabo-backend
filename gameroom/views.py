from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import  status as http_status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from gameroom.serializers import GameRoomSerializer
from helpers import Collection
from gameroom import services as gameroom_services
from gameroom import utils as gameroom_utils


# Create your views here.
class GameRoom(APIView):

    def get(self, request):
        req_obj  = Collection()
        req_obj.gameroom_uuid = request.query_params.get('room_uuid')
        gameroom = gameroom_utils.get_game_room_by_uuid(req_obj.gameroom_uuid)
        response = GameRoomSerializer(gameroom).data
        return Response(response, status=http_status.HTTP_200_OK)

    def post(self, request, format = None):
        print("here")
        req_obj = Collection()
        data = request.data
        req_obj.username = request.user
        response = gameroom_services.create_game_room(req_obj)
        return Response(response,  status = http_status.HTTP_200_OK)
        serializer = GameRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=http_status.HTTP_200_OK)
        else:
            return Response({'success': False, 'errors': serializer.errors}, status=http_status.HTTP_200_OK)

    def put(self, request, id):
        pass


@api_view(['POST'])
def join_gameroom(request, format= None):
    req_obj = Collection()
    req_obj.game_room_id = request.data['room_id']
    req_obj.username =  request.user
    response = gameroom_services.join_game_room(req_obj)
    return Response(response, status=http_status.HTTP_200_OK) 

@api_view(['POST'])
def start_game(request, format = None):
    req_obj = Collection()
    req_obj.game_room_id = request.data['room_id']
    req_obj.username =  request.user
    response = gameroom_services.start_game(req_obj)
    return Response(response, status=http_status.HTTP_200_OK)


@api_view(['POST'])
def find_winner(request, format=None):
    req_obj = Collection()
    req_obj.game_room_id = request.data['room_id']
    req_obj.username = request.user
    response = gameroom_services.find_winner(req_obj)
    return Response(response, status=http_status.HTTP_200_OK)

