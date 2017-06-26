from django.conf.urls import include,url
from . import views
app_name='music'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^allsongs$', views.allSongs, name='allSongs'),
    # url(r'^addAlbum', views.addAlbum, name='addAlbum'),
    url(r'^get_all_songs', views.get_all_songs, name='get_all_songs'),
    url(r'^get_all_album', views.get_all_album, name='get_all_album'),
    url(r'^addSong', views.addSong, name='addSong'),
    url(r'^addAlbum/$', views.addAlbum, name='addAlbum'),
    url(r'^(?P<album_id>[0-9]+)/addSong/$', views.addSong, name='addSong'),
    url(r'^get_ids', views.get_ids, name='get_ids'),
    url(r'^download_records', views.download_records, name='download_records'),
]