from django.urls import path, re_path
from .views import search_page, search_result

urlpatterns = [
    path('', search_page, name='search_page'),
    re_path(r'results/(?P<vvod>[0-9a-zA-Z._]{5,20})', search_result, name='search_result'),
]
