from django.conf.urls.defaults import *
from django.views.generic import list_detail
from testproject.testapp.views import default_person_info

urlpatterns = patterns('',
    (r'^$', list_detail.object_detail, default_person_info())
)
