from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def search_page(request):
    return render(request, 'search.html')


@require_http_methods(['GET'])
def search_result(request, vvod):
    maybe_result = [{'id': 1, 'res': 'ivan'},
                    {'id': 2, 'res': 'ivanov'},
                    {'id': 3, 'res': 'ivanova'}]
    return JsonResponse({f'results for {vvod}': maybe_result})
