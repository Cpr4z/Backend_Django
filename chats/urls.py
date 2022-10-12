from django.urls import path
from .views import chat_list, chat_category, chat_detail, chat_greeting


urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('category/<int:pk>/', chat_category, name='chat_category'),
    path('<chat_id>/', chat_detail, name='chat_detail'),
    path('greeting/', chat_greeting, name='chat_greeting')
]
