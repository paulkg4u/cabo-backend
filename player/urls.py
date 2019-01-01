from django.conf.urls import url
from player import views as player_views

urlpatterns = [
    url(r'^register/', player_views.Register.as_view()),
    url(r'^player/',player_views.PlayerView.as_view())
]