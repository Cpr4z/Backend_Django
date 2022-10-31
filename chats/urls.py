from django.urls import path, re_path
from .views import chat_list, chat_category


urlpatterns = [
    path('', chat_list, name='chat_list'),
    re_path(r'(?P<pk>[0-9]{2})/', chat_category, name='chat_category'),
]
