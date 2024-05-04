from django.urls import path,include
from app1 import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from views import add_audio
from .views import audio_list, add_audio, delete_audio

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path("register",views.register),
    path("logout",views.user_logout),
    path('audio_list', views.audio_list),
    path('add',views.add_audio ),
    path('delete<int:pk>', views.delete_audio),
    path('song/<int:id>',views.songpost),
    path('about',views.about ),
    path('contact',views.contact),
    path('search',views.search),
    path('forgetpass',views.forgetpass),
    path('like/<int:song_id>',views.like_song),
    path('playlist/',views.playlist ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




