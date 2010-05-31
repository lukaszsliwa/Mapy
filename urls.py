from settings import MEDIA_ROOT
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # static files
    url(r'^static/javascripts/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT + '/javascripts'}, name='javascripts'),
    url(r'^static/images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT + '/images'}, name='images'),
    url(r'^static/stylesheets/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT + '/stylesheets'}, name='stylesheets'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}, name='static'),

    url(r'^$', 'maps.views.new', name='root'),
    (r'^admin/', include(admin.site.urls)),
    (r'^mapy/', include('maps.urls')),
    (r'^czas/', include('stats.urls')),
    url(r'^tag/(?P<tag>.+)/$', 'maps.views.index', name='tag'),
    (r'^profil/', include('profiles.urls')),
    (r'^punkt/', include('points.urls')),

    (r'^komentarze/', include('comments.urls')),

    url(r'^nowy/$', 'profiles.views.new', name='new-profile'),
    url(r'^edytuj/$', 'profiles.views.edit', name='edit-profile'),
    url(r'^zaloguj/$', 'profiles.views.login', name='login'),
    url(r'^wyloguj/$', 'profiles.views.logout', name='logout'),
)
