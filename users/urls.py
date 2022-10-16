from django.urls import path, re_path
from .views import user_greeting, user_profile, user_first_greeting, user_online

urlpatterns = [
    re_path(r'thanks_for_registration/(?P<nickname>[0-9a-zA-Z]{5,20)/', user_first_greeting, name='first_greeting'),
    re_path(r'start_page/(?P<nickname>[0-9a-zA-Z]{5,20)/', user_greeting, name='greeting'),
    path(r'<pers_id>[0-9]{1,2}/(?P<nickname>[0-9a-zA-Z]{5,20})/', user_profile, name='user_profile'),
    path('online/', user_online, name='online_users'),
]
