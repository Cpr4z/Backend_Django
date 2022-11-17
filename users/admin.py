from django.contrib import admin
from users.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'reg_date', 'is_online')
    list_filter = ('is_online',)
    raw_id_fields = ('chats',)
    list_editable = ('is_online',)
    search_fields = ('nickname',)


admin.site.register(User, UserAdmin)
