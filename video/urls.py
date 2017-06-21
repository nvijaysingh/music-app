from django.conf.urls import include,url
from video import views
app_name='video'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addVideo', views.addVideo, name='addVideo'),
    url(r'^(?P<video_id>[0-9]+)/$', views.detail, name='detail'),
]