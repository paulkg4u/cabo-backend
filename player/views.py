from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status as http_status

from player.serialiazers import PlayerSerializer
from player.serialiazers import PlayerModelSerializer
from player import utils as player_utils
from helpers import Collection

# Create your views here.
class Register(APIView):

    def post(self, request):
        """

        :param request:
        :return:
        """
        data =request.data
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            new_player = serializer.save()
            print(new_player)
            return Response({'success': True}, status=http_status.HTTP_200_OK)
        else:
            print("not valid")
            return Response({'success': False, 'error': serializer.errors}, status= http_status.HTTP_200_OK)


class PlayerView(APIView):

    def get(self, request, format = None):
        print(request.user)
        print("here")
        req_obj = Collection()
        req_obj.username = request.user
        player = player_utils.get_player_by_username(req_obj.username)
        response = PlayerModelSerializer(player).data
        print(response)
        return Response(response, status=http_status.HTTP_200_OK)



