from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bossma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^masays/', include('masays.urls', namespace = 'masays')),
    url(r'^admin/', include(admin.site.urls)),
)
