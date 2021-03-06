from django.conf.urls import patterns, include, url
from mysite.view import hello, current_datetime
from mysite.score import hello 
from mysite.report import report 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$', hello),
	('^time/$', current_datetime),
	('^score/$', hello),
	('^time2/$', current_datetime),
	('^report/$', report)

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
