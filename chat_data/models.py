from django.db import models

class Message(models.Model):
	author_id = models.IntegerField()
	message_body = models.TextField(max_length=1024)
	date_time_created = models.DateTimeField(blank=True, null=True)
	date_time_edited = models.DateTimeField(blank=True, null=True)