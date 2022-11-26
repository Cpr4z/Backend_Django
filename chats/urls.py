from django.urls import path
from .views import (UserChats,
                    ChatMessages,
                    ChatDetails,
                    MessageDetails, )
from .views_old import (get_chat,
                        get_message,
                        update_chat,
                        update_message,
                        get_all_chats,
                        get_all_messages,
                        create_chat,
                        delete_chat,
                        create_message,
                        delete_member,
                        delete_message,
                        add_member,
                        read_message,)

urlpatterns = [
    path('owned_by_user/<int:pk>/', UserChats.as_view()),
    path('messages_in_chat/<int:chat_id>/', ChatMessages.as_view()),
    path('chat_details/<int:pk>/', ChatDetails.as_view()),
    path('message_details/<int:pk>/', MessageDetails.as_view()),
]
#urlpatterns = [
#     path('get_chat/', get_chat, name='get_chat'),
#     path('get_message/', get_message, name='get_message'),
#     path('update_chat/', update_chat, name='update_chat'),
#     path('update_message/', update_message, name='update_message'),
#     path('get_all_chats/', get_all_chats, name='get_all_chats'),
#     path('get_all_messages/', get_all_messages, name='get_all_messages'),
#     path('create_chat/', create_chat, name='create_chat'),
#     path('delete_chat/', delete_chat, name='delete_chat'),
#     path('create_message/', create_message, name='create_message'),
#     path('delete_message/', delete_message, name='delete_message'),
#     path('add_member/', add_member, name='add_member'),
#     path('delete_member/', delete_member, name='delete_member'),
#     path('read_message/', read_message, name='read_message')
#]
