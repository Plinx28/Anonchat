from django.shortcuts import render
from .models import Message
from .forms import MessagePostForm, MessageGetForm
from django.http import HttpResponseNotFound
from .services import *

def index(request):
    return render(request, 'chat/index.html', {'notes_len': len(Message.objects.order_by('id'))})


def createMessage(request):
    error = ''
    if request.method == 'POST':
        form = MessagePostForm(request.POST)
        if form.is_valid(): return render(request, 'chat/hash.html', {'note_hash': create_message_and_get_hash(form)})
        else: error = 'invalid enter'

    form = MessagePostForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'chat/create.html', data)


def readMessage(request):   
    if request.method == 'GET':
        form = MessageGetForm(request.GET)
        if form.is_valid(): return render(request, 'chat/detail.html', get_message_and_delete(form))

    return render(request, 'chat/read.html', {'form': MessageGetForm()})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')