from django.conf.urls import url

from gameroom import views as gameroom_views

urlpatterns = [
    url(r'^gameroom/$', gameroom_views.GameRoom.as_view()),
    url(r'^gameroom/(?P<id>[A-Z0-9]{8})$', gameroom_views.GameRoom.as_view()),
    url(r'^join_gameroom/$', gameroom_views.join_gameroom),
    url(r'^start_game/$', gameroom_views.start_game),
    url(r'^find_winner/$',gameroom_views.find_winner)
]