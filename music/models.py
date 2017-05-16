from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
     return self.album_title+"--" + self.artist+"-- "+ self.genre
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE )
    #on_delete=models.CASCADE is used to delete all songs in a album if album is deleted.
    #ForeignKey is used to link song with album having some primary key let's say 1.
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    song_file = models.FileField()

    def __str__(self):
        return self.song_title

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''
