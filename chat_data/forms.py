from django import forms

from .models import Message, MessageAuthor

class PostMessage(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('message_body',)