from django import urls
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import  URLPattern, path
from . import views
urlpatterns = [
        path('getSongList/', views.getSongList.as_view(), name='getSongList'),
        path('createSong/', views.Create_Song.as_view(), name='createSong'),
        path('updateSong/', views.Update_Song.as_view(), name='updateSong'),
        path('deleteSong/', views.deleteSong.as_view(), name='deleteSong'),
    ]
