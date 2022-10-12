from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


def chat_list(request):
    return JsonResponse({'chats': []})
# Create your views here.

def chat_category(request, pk):
    if request.metod == "GET"
    return JsonResponse({'chat_pk': pk})
def chat_detail(request):
    return JsonResponse({'chat_details': []})

def chat_greeting(request):
    return render(request, 'index.html',)