from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns() #static file
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT) #media file