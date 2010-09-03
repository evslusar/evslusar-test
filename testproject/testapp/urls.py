from django.conf.urls.defaults import *

from django.views.generic import list_detail
from testapp.views import *

urlpatterns = patterns('',
    (r'^$', list_detail.object_detail, default_person_info()),
    (r'^log/$', list_detail.object_list, request_log_info()),
    (r'^edit/$', edit_view),
    (r'^settings/$', settings_view),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', logout_view)
)

