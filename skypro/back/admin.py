from django.contrib import admin
from back.models import UserFile, FileLogs


@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'file', 'author', 'status']
    list_filter = ['author', 'status']
