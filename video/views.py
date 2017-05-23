# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'video/index.html', context)