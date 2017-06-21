# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .forms import VideoForm
from .models import Video
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def index(request):
    newlist =[]
    videos = Video.objects.all()
    for video in videos:
        full_url = ''.join(['http://', get_current_site(request).domain, '/', video.video_file.url])
        newlist.append({'video':video.video_title,'url':full_url,'key':video.pk})
    context = {'videos':newlist}
    return render(request, 'video/index.html', context)

def detail(request,video_id):
  newlist = []
  video= get_object_or_404(Video, pk=video_id)
  full_url = ''.join(['http://', get_current_site(request).domain, '/', video.video_file.url])
  print  video
  print full_url
  newlist.append({'video': video.video_title, 'url': full_url, 'key': video.pk})
  print newlist
  context = {'videos': newlist}
  return render(request, "video/detail.html",context)


def addVideo(request):
  form = VideoForm(request.POST or None, request.FILES or None)
  if form.is_valid():
        video = form.save(commit=False)
        video.video_file = request.FILES['video_file']
        print video
        video.save()
        link = '/video/'
        return HttpResponseRedirect(link)
  context ={}
  return render(request, 'video/addVideo.html', context)