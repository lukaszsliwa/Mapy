from django.conf.urls.defaults import *

urlpatterns = patterns('maps.views',
    url(r'^$', 'index', name='maps'),
    url(r'^nowa/$', 'new', name='new-map'),
    url(r'^(?P<map_id>[0-9]+)/(?P<slug>.*)/$', 'show', name='map'),
    url(r'^lubie/(?P<map_id>[0-9]+)/(?P<slug>.*)$', 'like', name='like-map')
)
