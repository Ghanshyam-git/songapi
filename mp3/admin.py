from django.contrib import admin
from mp3.models import *
# Register your models here.
@admin.register(Song)
class songAdmin(admin.ModelAdmin):
    list_display=['songname','file']