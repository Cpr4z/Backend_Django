from django.urls import path, re_path
from .views import messenger_greeting, messenger_Log_In, messenger_recovering, messenger_registration


urlpatterns = [path('', messenger_greeting, name='messenger_greeting'),
               path('registration/', messenger_registration, name='messenger_registration'),
               path('LogIn/', messenger_Log_In, name='messenger_Log_In'),
               path('recovering/', messenger_recovering, name='messenger_recovering'),
]
