from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'projectx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('allauth.urls')),
)
