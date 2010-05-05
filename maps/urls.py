from django.conf.urls.defaults import *

urlpatterns = patterns('maps.views',
    url(r'^$', 'index', name='maps'),
    url(r'^nowa/$', 'new', name='new-map'),
    url(r'^(?P<slug>.*)/$', 'show', name='map'),
)
