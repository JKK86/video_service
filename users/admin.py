from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Profile
from videos.admin import UserMovieAdminInline

admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'membership']
    inlines = [UserMovieAdminInline, ]

