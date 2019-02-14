from django.db import models
from datetime import date
from django.utils import timezone

class MessageAuthor(models.Model):
	user_id = models.IntegerField()
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	image_icon_url = models.URLField()

class Message(models.Model):
	author_id = models.IntegerField()
	message_body = models.TextField(max_length=1024)
	date_time_created = models.DateTimeField(blank=True, null=True)
	date_time_edited = models.DateTimeField(blank=True, null=True)