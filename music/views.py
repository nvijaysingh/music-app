from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album
from django.views.decorators.csrf import csrf_exempt
import json
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
  return render(request, "music/detail.html",{'album':album})

def mainPage(request):

    return HttpResponseRedirect('/music/')
def allSongs(request):
    album = Album.objects.all()
    context = {'album': album}
    return render(request, 'music/allSongs.html', context)


@csrf_exempt
def addAlbum(request):
        album = json.loads(request.body)
        result = dict()
        if Album.objects.filter(album_title = album['album_title']).count() <= 0:
           savealbum = Album(artist = album['artist'], album_title= album['album_title'], genre= album['genre'])
           savealbum.save()
        result['status'] = 'success'
        return HttpResponse(json.dumps(result), content_type="application/json")