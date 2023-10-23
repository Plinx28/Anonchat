from django.urls import path, re_path

from . import views
# from views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.createMessage, name='message-create'),
    path('read/', views.readMessage, name='message-read')
]

handler404 = views.pageNotFound