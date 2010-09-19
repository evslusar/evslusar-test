from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic import list_detail

from testapp.views import *
from testapp.requestviews import request_log_view, edit_priority_view


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', list_detail.object_detail, default_person_info()),
    (r'^log/$', request_log_view),
    (r'^edit_priority/$', edit_priority_view),
    (r'^edit/$', edit_view),
    (r'^edit_ajax/$', edit_ajax_view),
    (r'^settings/$', settings_view),
    (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    (r'^logout/$', logout_view),
    (settings.ADMIN_URL_PATTERN, include(admin.site.urls)))
