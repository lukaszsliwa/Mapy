from django.conf.urls.defaults import *

urlpatterns = patterns('stats.views',
    url(r'^nowy/(?P<map_id>[0-9]+)/$', 'new', name='new-time'),
    url(r'^dodaj/(?P<map_id>[0-9]+)/$', 'add', name='add-time'),
)
