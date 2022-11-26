from django.http import JsonResponse
from users.models import User
from django.views.decorators.http import require_http_methods
# Create your views here.


@require_http_methods(['GET'])
def get_user(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if user is not None:
        chats = user.chats.all().values()
        return JsonResponse({
            'ok': True,
            'result': {
                'id': user.id,
                'username': user.username,
                'chats': list(chats),
            }
        })
    return JsonResponse({
        'ok': False,
        'result': f'user with id={user_id} does not exists',
    })

