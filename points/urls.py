from django.conf.urls.defaults import *

urlpatterns = patterns('points.views',
    url(r'^nowy/$', 'new', name='new-point'),
)
