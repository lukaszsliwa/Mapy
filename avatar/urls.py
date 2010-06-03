from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('avatar.views',
    url('^dodaj/$', 'add', name='avatar_add'),
    url('^zmien/$', 'change', name='avatar_change'),
    url('^usun/$', 'delete', name='avatar_delete'),
    url('^generuj/(?P<user>[\+\w]+)/(?P<size>[\d]+)/$', 'render_primary', name='avatar_render_primary'),
)
