from django.contrib import admin
from chats.models import Chat, Message
# Register your models here.


class ChatAdmin(admin.ModelAdmin):
    raw_id_fields = ('members',)
    search_fields = ('create_date',)
    exclude = ('mes_amount', 'is_group_chat')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'sent_from', 'sent_to', 'is_delivered')
    list_filter = ('is_delivered',)
    raw_id_fields = ('chat_id', 'sent_from', 'sent_to')
    list_editable = ('is_delivered',)
    search_fields = ('text',)


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
