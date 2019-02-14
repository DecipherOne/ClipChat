from django.db import models

class MessageAuthor(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    image_icon_url = models.URLField()

class Message(models.Model):
    author_id = models.IntegerField()
    message_parent_id = models.IntegerField()
    message_body = models.TextField(max_length=1024)
    message_id = models.IntegerField()
