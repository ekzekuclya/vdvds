from django.db import models


class TelegramUser(models.Model):
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username if self.username else "None"


class Trigger(models.Model):
    chat_id = models.IntegerField()
    message_id = models.IntegerField()
    trigger_name = models.CharField(max_length=255)


