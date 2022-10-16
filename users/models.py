from django.db import models
import datetime

# Create your models here.


class Users(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, default='qwerty123')
    reg_date = models.DateField(auto_now_add=True)
    is_online = models.BooleanField(default=True)
    is_photo = models.BooleanField(default=False)
    user_info = models.CharField(max_length=200, unique=True)
