from django import forms

from .models import Message

class PostMessage(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('message_body',)