from django import forms
from django.contrib.auth.models import User

from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'genre', 'album_logo',)


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('file_type','song_title', 'song_file',)