from django.db import models
from users.models import Users
import datetime
# Create your models here.


class Chats(models.Model):
    first_user = models.ForeignKey(Users, related_name='first_user', on_delete=models.SET_NULL, null=True, blank=True)
    second_user = models.ForeignKey(Users, related_name='second_user', on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    mes_amount = models.IntegerField(default=0)


class Messages(models.Model):
    chat_id = models.ForeignKey(Chats, on_delete=models.SET_NULL, null=True, blank=True)
    sent_from = models.ForeignKey(Users, related_name='sent_from', on_delete=models.SET_NULL, null=True, blank=True)
    sent_to = models.ForeignKey(Users, related_name='sent_to', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length=400, default='')
    sent_time = models.DateTimeField(auto_now_add=True)
