from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stream_app.views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', 'stream_app.views.register'),
    url(r'^stream/$', 'stream_app.views.login_landing', name='landing_page'),
    url(r'^stream/list$', 'stream_app.views.user_streams', name='stream_list'),
    url(r'^stream/save$', 'stream_app.views.stream_save', name='stream_save'),
    url(r'^stream/show/(?P<stream_name>[a-z]+)$', 'stream_app.views.stream_viewer', name='stream_list'),
    url(r'^word/show/(?P<word>[a-z]+)$', 'stream_app.views.word_viewer', name='show_word'),
    url(r'^show_me/$', 'stream_app.views.show_me', name='show_me'),
    # url(r'^$', 'streaming.views.home', name='home'),
    # url(r'^streaming/', include('streaming.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
