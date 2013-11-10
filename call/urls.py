from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^play/$', 'play.views.play', name='play'),
    url(r'^trigger/$', 'play.views.trigger', name='trigger'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
