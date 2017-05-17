from django.conf.urls import include,url
from django.conf import settings
from music import views
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

   url(r'^admin/', admin.site.urls),
   url(r'^$', views.mainPage, name='mainPage' ),
   url(r'^music/', include('music.urls')),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
