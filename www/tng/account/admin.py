from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from tng.account.models import Computer, Console, Game, Monitor, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]

admin.site.register(Computer)
admin.site.register(Console)
admin.site.register(Game)
admin.site.register(Monitor)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)