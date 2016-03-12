from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from gallery.views import index, customhomes, newconstruction, roofing, remodeling, concrete, snowremoval, gallery, album, contact, thankyou
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    url(r'^customhomes$', customhomes),
    url(r'^newconstruction$', newconstruction),
    url(r'^roofing$', roofing),
    url(r'^remodeling$', remodeling),
    url(r'^concrete$', concrete),
    url(r'^snowremoval$', snowremoval),
    url(r'^gallery$', gallery),
    url(r'^gallery/(?P<pk>\d)$', album),
    url(r'^contact$', contact),
    url(r'^thankyou$', thankyou),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
