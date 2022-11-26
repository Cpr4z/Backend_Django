from rest_framework import generics

from .models import Chat, Message
from users.models import User
from .serializers import ChatSerializer, MessageSerializer
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from .permissions import AdminOrAuthor


#{"user_id": 2} GET POST
class UserChats(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return Chat.objects.filter(members=user_id)


class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
    ''' обрабатывает get, put, patch, delete запросы '''
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (AdminOrAuthor,)


class ChatMessages(generics.ListCreateAPIView):
    ''' обрабатывает get и post запросы '''
    serializer_class = MessageSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat_id=chat_id)


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    ''' обрабатывает get, put, patch, delete запросы '''
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AdminOrAuthor,)


