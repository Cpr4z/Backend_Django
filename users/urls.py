from django.urls import path
from .views import user_profile, user_greeting, user_online

urlpatterns = [
    path('', user_greeting, name='greeting'),
    path('<user_id>', user_profile, name='user_id'),
    path('online/', user_online, name='online_users'),
]