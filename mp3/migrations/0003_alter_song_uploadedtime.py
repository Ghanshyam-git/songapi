# Generated by Django 3.2.10 on 2022-05-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp3', '0002_alter_song_uploadedtime_alter_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='UploadedTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
