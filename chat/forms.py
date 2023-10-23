from .models import Message
from django.forms import ModelForm, TextInput, Textarea
# from django import forms - better, when u use simple forms such as Form
# затем это просто летит во views, там создается объект этого класса и передаётся в data-dict в render -> html


class MessagePostForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'secret_phrase']

        widgets = {
            'secret_phrase': TextInput(attrs={
                'id': 'secret-phrase',
                'placeholder': 'Enter the secret phrase'
            }),
            'text': Textarea(attrs={
                'id': 'message',
                'placeholder': 'Message text'
            })
        }

class MessageGetForm(ModelForm):
    class Meta:
        model = Message
        fields = ['secret_phrase', 'note_hash']

        widgets = {
            'secret_phrase': TextInput(attrs={
                'id': 'input-secret-phrase',
                'placeholder': 'Enter the secret phrase'
            }),
            'note_hash': TextInput(attrs={
                'id': 'input-hash',
                'placeholder': 'Enter the hash code'
            })
        }