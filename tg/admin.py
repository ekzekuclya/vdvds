from django.contrib import admin
from .models import Trigger, TelegramUser


@admin.register(Trigger)
class TriggerAdmin(admin.ModelAdmin):
    list_display = ['trigger_name']


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username' if 'username' else 'None']
