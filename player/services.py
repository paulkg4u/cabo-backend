from player.models import Player


def create_player_from_social_login(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        user.first_name =  response['first_name']
        user.last_name = response['last_name']
        user.email = response['email']
        user.save()
        existing_player = Player.objects.filter(user__username = user.username)
        if len(existing_player) == 1:
            existing_player[0].pic_url = response['picture']['data']['url']
            existing_player[0].save()
        else:
            Player.objects.create(
                user = user,
                pic_url = response['picture']['data']['url']
            )
    elif backend.name == 'google-plus':
        user.first_name = response.get('name').get('givenName')
        user.last_name = response.get('name').get('familyName')
        user.email = response.get('emails')[0].get('value')
        user.save()
        existing_player = Player.objects.filter(user__username = user.username)
        if len(existing_player) == 1:
            existing_player[0].pic_url = response.get('image').get('url')
            existing_player[0].save()
        else:
            Player.objects.create(
                user = user,
                pic_url = response.get('image').get('url')
            )


