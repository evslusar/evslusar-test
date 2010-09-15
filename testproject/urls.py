from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('testproject.testapp.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.STATIC_MEDIA_PREFIX,
        'django.views.static.serve',
        {'document_root': settings.STATIC_MEDIA_ROOT}),
    )
