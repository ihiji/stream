from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stream_app.views.index'),
    url(r'^stream/$', 'stream_app.views.index', name='landing_page'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'streaming.views.home', name='home'),
    # url(r'^streaming/', include('streaming.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
