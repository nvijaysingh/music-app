from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album,Song
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import AlbumForm, SongForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.conf import settings
def index(request):
   # /music/
  all_albums = Album.objects.all()

  context ={'all_albums':all_albums}
  return render(request, 'music/index.html', context)
  # template= loader.get_template('music/index.html')
  #return HttpResponse(template.render(context, request))
   # /music/712/


def detail(request,album_id):
 #return HttpResponse("<h2>Details of album id: "+str(album_id)+"</h2>")
  #try:
   #   album=Album.objects.get(id=album_id)
  #except Album.DoesNotExist:
   #   raise Http404('Album Does Not Exist')
  album= get_object_or_404(Album, pk=album_id)
  songs_list = Song.objects.filter(album=album)
  print songs_list
  return render(request, "music/detail.html",{'album':album,'songs':songs_list})

def mainPage(request):
    return render(request, "music/mainPage.html",)

def addAlbum(request):
  form = AlbumForm(request.POST or None, request.FILES or None)
  if form.is_valid():
        album = form.save(commit=False)
        album.album_logo = request.FILES['album_logo']
        print album
        album.save()
        return HttpResponseRedirect('/music/')
  return render(request, 'music/addAlbum.html')    

def addSong(request,album_id):
  form = SongForm(request.POST or None, request.FILES or None)
  album = get_object_or_404(Album, pk=album_id)
  print album
  if form.is_valid():
        song = form.save(commit=False)
        song.album = album
        song.song_file = request.FILES['song_file']
        print song
        song.save()
        link = '/music/'+album_id
        return HttpResponseRedirect(link)
  all_albums = Album.objects.all()
  context ={'all_albums':all_albums}      
  return render(request, 'music/addSong.html', context)    

def allSongs(request):
    songs_list = []
    newlist2=[]
    album = Album.objects.all()
    # print album
    for song in album:
          new_song=Song.objects.filter(album=song)
          for song2 in new_song:
               full_url = ''.join(['http://', get_current_site(request).domain, '/', song2.song_file.url])
               songs_list.append({'song_title':song2.song_title,'file_type':song2.file_type,'id':song2.pk,'url':full_url})
          newlist2.append({'album_title':song.album_title,'album_logo_url':song.album_logo.url,'album_songs':songs_list})
          songs_list = []
    # print newlist2
    context = {'album':newlist2}
    return render(request, 'music/allSongs.html', context)

# @csrf_exempt
# def addAlbum(request):
#   if request.method == "POST":
#         file = request.FILES.get('img')
#         print file
#         # album = json.loads(request.body or None, request.FILES or None)
#         result = dict()
#         # print album
#         # if Album.objects.filter(album_title = album['album_title']).count() <= 0:
#         #     savealbum = Album(artist = album['artist'], album_title= album['album_title'], genre= album['genre'],album_logo=album['logo'])
#         #     savealbum.save()
#         result['status'] = 'success'
#         return HttpResponse(json.dumps(result), content_type="application/json")
        
@csrf_exempt
def get_all_songs(request):
    newlist = []
    result = dict()
    new_song = Song.objects.get(pk=request.GET.get('id'))
    full_url = ''.join(['http://', get_current_site(request).domain, '/', new_song.song_file.url])
    newlist.append({'song': full_url,'name':new_song.song_title,'length':new_song.song_file.size, 'pk': new_song.pk})
    # print newlist
    result['list'] = newlist
    return HttpResponse(json.dumps(result), content_type="application/json")

@csrf_exempt
def get_all_album(request):
    newlist = []
    newlist2 = []
    result = dict()
    new_song = Album.objects.all()
    for new in new_song:
      newlist.append({'album': new.album_title, 'pk': new.pk})
    newlist2.append({'list_of_albums':newlist})
    # print newlist2
    result['list'] = newlist2
    return HttpResponse(json.dumps(result), content_type="application/json")

# @csrf_exempt
# def addSong(request):
#         album2 = json.loads(request.body or None, request.FILES or None)
#         result = dict()
#         print album2
#         new_album=Album.objects.get(album_title = album2['album'])
#         savesong = Song(album = new_album, file_type= album2['file_type'], song_title= album2['song_title'])
#         savesong.save()
#         result['status'] = 'success'
#         return HttpResponse(json.dumps(result), content_type="application/json")

@csrf_exempt
def get_ids(request):
    newlist = []
    result = dict()
    new_song2 = Song.objects.all()
    for new in new_song2:
      newlist.append(new.pk)
    print newlist
    result['list'] = newlist
    return HttpResponse(json.dumps(result), content_type="application/json")

