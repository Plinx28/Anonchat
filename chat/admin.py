from django.contrib import admin

# Register your models here.
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'secret_phrase', 'note_hash', 'create_time')
    list_display_links = ('id', 'secret_phrase')
    search_fields = ('secret_phrase', 'note_hash')

admin.site.register(Message, MessageAdmin)