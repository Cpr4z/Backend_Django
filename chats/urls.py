from django.urls import path, re_path
from .views import chat_list, chat_category, chat_greeting


urlpatterns = [
    path('', chat_greeting, name='chat_greeting'),
    path('chat_list', chat_list, name='chat_list'),
    re_path(r'^chat_list/(?P<pk>[0-9]{2})/', chat_category, name='chat_category'),
]
