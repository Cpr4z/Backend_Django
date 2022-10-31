from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
# Create your views here.


@require_http_methods(['GET'])
def messenger_greeting(request):
    return render(request, 'index.html')


@require_http_methods(['GET', 'POST'])
def messenger_registration(request):
    return render(request, 'registration.html')



@require_http_methods(['GET', 'POST'])
def messenger_Log_In(request):
    return render(request, 'Log_In.html')


@require_http_methods(['GET', 'POST'])
def messenger_recovering(request):
    return render(request, 'recovering.html')

