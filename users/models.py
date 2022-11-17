from django.db import models
from chats.models import Chat
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    password = models.CharField(max_length=50, default='qwerty123')
    reg_date = models.DateField(auto_now_add=True)
    is_online = models.BooleanField(default=True)
    is_photo = models.BooleanField(default=False)
    user_info = models.CharField(max_length=200, unique=True)
    chats = models.ManyToManyField(Chat, blank=True, verbose_name='Чаты')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-reg_date',)

    def __str__(self):
        return self.nickname
