from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album

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

