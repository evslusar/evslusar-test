from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from testapp.models import *
from testapp.contextprocs import settings_context_proc


def default_person():
    return Person.objects.get(pk=1)


def default_person_info():
    p = default_person()
    info = {'queryset': Person.objects.all(),
        'object_id': p.pk,
        'template_name': 'person_detail.html'}
    return info


def request_log_info():
    all_requests = HttpRequestLog.objects.all()
    return {'queryset': all_requests.order_by('-request_date'),
        'template_name': 'request_log_list.html'}


def settings_view(request):
    context = RequestContext(request, {}, [settings_context_proc])
    return render_to_response('view_settings.html', context_instance=context)
