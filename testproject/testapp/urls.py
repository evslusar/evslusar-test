from django.conf.urls.defaults import *

from django.views.generic import list_detail
from testapp.views import default_person_info
from testapp.views import request_log_info
from testapp.views import edit_view

urlpatterns = patterns('',
    (r'^$', list_detail.object_detail, default_person_info()),
    (r'^log/$', list_detail.object_list, request_log_info()),
    (r'^edit/$', edit_view)
)

