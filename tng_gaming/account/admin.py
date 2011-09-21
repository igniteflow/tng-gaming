from django.contrib import admin
from account.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]
    

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)