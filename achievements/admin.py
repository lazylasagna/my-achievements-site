from django.contrib import admin
from .models import Achievement, Like


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'created_at')
    list_filter = ('created_at',)
