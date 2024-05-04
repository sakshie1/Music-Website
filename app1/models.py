
# models.py
from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    singer = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    pimage = models.ImageField(upload_to='image')
    audio_file = models.FileField(upload_to='audio_files/')

    # Add a field to track the number of likes
    likes = models.ManyToManyField(User, related_name='liked_songs', blank=True)

    def __str__(self):
        return self.name

