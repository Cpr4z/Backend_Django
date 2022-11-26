from django.contrib import admin
from users.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'reg_date', 'is_online')
    list_filter = ('is_online',)
    raw_id_fields = ('chats',)
    search_fields = ('username', 'date_joined')


admin.site.register(User, UserAdmin)
