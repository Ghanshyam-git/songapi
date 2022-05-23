from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator



class Song(models.Model):
    songname = models.CharField(max_length=100)
    duration = models.PositiveBigIntegerField()
    UploadedTime = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='song',validators=[FileExtensionValidator( ['mp3'] ) ] ) 
