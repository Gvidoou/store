from django.conf.urls import patterns, include, url
from django.contrib import admin
from Products import urls

urlpatterns = patterns(
    '',
    # url(r'^$', , name='home'),
    url(r'products/', include(urls)),
    url(r'^admin/', include(admin.site.urls)),
)

