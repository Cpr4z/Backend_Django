from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def user_greeting(request, nickname):
    return JsonResponse({'Hello:': nickname})

def user_profile(request, id):
    return JsonResponse({'user_is':id})

def user_online(request):
    return JsonResponse({'online users:':[]})


