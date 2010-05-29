from django.conf.urls.defaults import *

urlpatterns = patterns('points.views',
    url(r'^nowy/$', 'new', name='new-point'),
    url(r'^(?P<SWLat>[0-9]+.[0-9]+)/(?P<SWLng>[0-9]+.[0-9]+)/(?P<NELat>[0-9]+.[0-9]+)/(?P<NELng>[0-9]+.[0-9]+)/$', 'show', name='points-show'),
)
