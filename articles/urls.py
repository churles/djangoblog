from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list),
    url(r'^about$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"), 
        # (?P<slug>[\w-]+)/ // capture slug
        # [\w-] // any type of letter, number and hypen
        # + // any length of string
]

