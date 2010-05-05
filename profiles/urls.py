from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^$', 'index', name='my-profile'),

    url(r'^(?P<username>.+)/$', 'show', name='profile'),
)
