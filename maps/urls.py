from django.conf.urls.defaults import *

urlpatterns = patterns('maps.views',
    url(r'^$', 'index', name='maps'),
    url(r'^nowa/$', 'new', name='new-map'),
    url(r'^(?P<map_id>[0-9]+)/(?P<slug>.*)/$', 'show', name='map'),
    url(r'^(?P<SWLat>[0-9]+.[0-9]+)/(?P<SWLng>[0-9]+.[0-9]+)/(?P<NELat>[0-9]+.[0-9]+)/(?P<NELng>[0-9]+.[0-9]+)/$', 'maps_in_bounds', name='maps-show'),
    url(r'^lubie/(?P<map_id>[0-9]+)/(?P<slug>.*)$', 'like', name='like-map'),
    url(r'^nie-lubie/(?P<map_id>[0-9]+)/(?P<slug>.*)$', 'unlike', name='unlike-map')
)
