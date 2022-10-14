from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(["GET"])
def user_first_greeting(request, nickname):
    return render(request, 'new_user.html', {'name': nickname})

@require_http_methods(['GET'])
def user_greeting(request, nickname):
    return JsonResponse({'Hello': nickname})

@require_http_methods(['GET'])
def user_profile(request, pers_id, nickname):
    return JsonResponse({'user_id': pers_id,
                         'user_nickname': nickname, })

@require_http_methods(['GET'])
def user_online(request):
    return JsonResponse({'online users': []})


