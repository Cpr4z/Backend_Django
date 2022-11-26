from django.urls import path
from .views import (AddUserAsMember, DeleteUserFromChat)
from .views_old import get_user

urlpatterns = [
    path('user/<int:pk>/add_to_chat/<int:user_id>/', AddUserAsMember.as_view()),
    path('user/<int:pk>/delete_from_chat/<int:chat_id>/', DeleteUserFromChat.as_view())
]
#urlpatterns = [
#    path('<int:user_id>/', get_user, name='get_user')
#]
