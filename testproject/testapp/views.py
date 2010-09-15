from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from testapp.models import Person, HttpRequestLog
from testapp.forms import PersonForm


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


def edit_view(request):
    form = PersonForm()
    if request.method == 'GET':
        form = PersonForm(instance=default_person())
    elif request.method == 'POST':
        form = PersonForm(request.POST, instance=default_person())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render_to_response('person_edit.html', {'form': form})
