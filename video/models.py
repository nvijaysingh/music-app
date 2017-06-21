# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.db import models

# Create your models here.
class Video(models.Model):
    video_title = models.CharField(max_length=100)
    video_file = models.FileField()

    def __str__(self):
        return self.video_title


@receiver(pre_delete, sender=Video)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.song_file.delete(False)