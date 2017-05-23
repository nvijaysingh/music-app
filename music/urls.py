from django.conf.urls import include,url
from . import views
app_name='music'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^allsongs$', views.allSongs, name='allSongs'),
    url(r'^addAlbum', views.addAlbum, name='addAlbum'),
]