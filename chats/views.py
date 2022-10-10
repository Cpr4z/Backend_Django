from django.shortcuts import render
from django.http import JsonResponse


def chat_list(request):
    return JsonResponse({'chats': []})
# Create your views here.

def chat_category(request, pk):
    return JsonResponse({'chat_pk': pk})
def chat_detail(request):
    return JsonResponse({'chat_details': []})
