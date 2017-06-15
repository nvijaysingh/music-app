from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
     return self.album_title+"--" + self.artist+"-- "+ self.genre

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album" )
    #on_delete=models.CASCADE is used to delete all songs in a album if album is deleted.
    #ForeignKey is used to link song with album having some primary key let's say 1.
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    song_file = models.FileField()

    def __str__(self):
        return self.song_title

@receiver(pre_delete, sender=Album)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.album_logo.delete(False)

@receiver(pre_delete, sender=Song)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.song_file.delete(False)

