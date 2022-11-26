from django.db import models
from django.conf import settings


class Chat(models.Model):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name='Участники чата')
    is_group_chat = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания чата')
    mes_amount = models.IntegerField(default=0, verbose_name='Количество сообщений в чате')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ('-create_date',)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Номер чата')
    sent_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_from_message', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отправлено от')
    sent_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_to_message', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отправлено кому')
    text = models.CharField(max_length=400, default='')
    sent_time = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')
    is_delivered = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False, verbose_name='Прочитано или нет')

    def __str__(self):
        return f'{self.sent_from} to {self.sent_to}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-sent_time',)
