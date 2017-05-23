from django.conf.urls import include,url
from video import views
app_name='video'
urlpatterns = [
    url(r'^$', views.index, name='index'),

]