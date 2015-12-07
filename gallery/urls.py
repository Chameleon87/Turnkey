from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gallery.views.index'),
    url(r'^customhomes$', 'gallery.views.customhomes'),
    url(r'^newconstruction$', 'gallery.views.newconstruction'),
    url(r'^roofing$', 'gallery.views.roofing'),
    url(r'^remodeling$', 'gallery.views.remodeling'),
    url(r'^concrete$', 'gallery.views.concrete'),
    url(r'^snowremoval$', 'gallery.views.snowremoval'),
    url(r'^gallery$', 'gallery.views.gallery'),
    url(r'^gallery/(?P<pk>\d)$', 'gallery.views.album'),
    url(r'^contact$', 'gallery.views.contact'),
    url(r'^thankyou$', 'gallery.views.thankyou'),
    url(r'^admin/', include(admin.site.urls)),
    
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
