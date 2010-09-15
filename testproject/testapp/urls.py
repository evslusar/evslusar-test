from django.conf.urls.defaults import *
from django.views.generic import list_detail

from testapp.views import default_person_info, request_log_info


urlpatterns = patterns('',
    (r'^$', list_detail.object_detail, default_person_info()),
    (r'^log/$', list_detail.object_list, request_log_info()))
