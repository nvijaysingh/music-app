from django import forms
from django.contrib.auth.models import User

from .models import Video


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('video_title','video_file',)