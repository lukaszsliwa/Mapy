from django.conf.urls.defaults import *

urlpatterns = patterns('comments.views',
    url(r'^$', 'index', name='comments'),
    url(r'^(?P<map_id>[0-9]+)$', 'create', name='create-comment'),
)
