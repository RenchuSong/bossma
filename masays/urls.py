from django.conf.urls import patterns, url
from masays import views

urlpatterns = patterns('',
	# ex: /masays/
	url(r'^$', views.index, name = 'index'),
	# ex: /masays/mobile/
	url(r'^mobile/$', views.mobile, name = 'mobile'),
	# ex: /masays/web/
	url(r'^web/$', views.web, name = 'web'),

)