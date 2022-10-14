from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def chat_greeting(request):
    return render(request, 'index.html',)

@require_http_methods(['GET'])
def chat_list(request):
    chats = [{'id': 1, 'title': 'mom'},
             {'id': 2, 'title': 'Bob'}]
    return JsonResponse({'all chats': chats})
# Create your views here.

@require_http_methods('GET')
def chat_category(request, pk):
    history = [{'id': 1, 'message': 'hello'},
                   {'id': 2, 'message': 'Hi!'}]
    return JsonResponse({f'chat id {pk} log': history})



