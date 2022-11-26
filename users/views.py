from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .permissions import AdminOrAuthor


class AddUserAsMember(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return User.objects.filter(id=user_id)


    def update(self, request, *args, **kwargs):
        user = self.get_object()
        chat_id = self.kwargs.get('chat_id')
        chat = user.chats.filter(id=chat_id).first()
        if chat is None:
            user.chats.add(chat_id)
            return Response({'ok': True}, status=status.HTTP_200_OK)

        return Response({
            'ok': False,
            'result': 'user already in chat'
        }, status=status.HTTP_403_FORBIDDEN)


class DeleteUserFromChat(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return User.objects.filter(id=user_id)

    # curl -X PUT -d '{"username":"dmitrii2","chat_id": 2}' http://127.0.0.1:8000/api/v1/users/user/2/delete_from_chat/ -H 'Content-Type: application/json'
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        chat_id = self.kwargs.get('chat_id')
        chat = user.chats.filter(id=chat_id).first()
        if chat is None:
            return Response({
                'ok': False,
                'result': 'user already deleted'
            }, status=status.HTTP_403_FORBIDDEN)

        user.chats.remove(chat_id)
        return Response({'ok': True}, status=status.HTTP_200_OK)
