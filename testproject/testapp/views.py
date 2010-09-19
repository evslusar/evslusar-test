from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, \
    HttpResponseForbidden, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext

from testapp.models import Person
from testapp.forms import PersonForm, AjaxPersonForm
from testapp.contextprocs import settings_context_proc


def default_person():
    return Person.objects.get(pk=1)


def default_person_info():
    p = default_person()
    info = {'queryset': Person.objects.all(),
        'object_id': p.pk,
        'template_name': 'person_detail.html'}
    return info


@login_required
def edit_view(request):
    form = AjaxPersonForm()
    if request.method == 'GET':
        form = AjaxPersonForm(instance=default_person())
    elif request.method == 'POST':
        form = AjaxPersonForm(request.POST, instance=default_person())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render_to_response('person_edit.html',
        {'form': form}, context_instance=RequestContext(request))


def edit_ajax_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = AjaxPersonForm(request.POST, instance=default_person())
            if form.is_valid():
                form.save()
            return HttpResponse(form.as_p_with_submit())
        else:
            return HttpResponseForbidden('Login required!')
    else:
        return HttpResponseNotAllowed(['POST'])


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def settings_view(request):
    context = RequestContext(request, {}, [settings_context_proc])
    return render_to_response('view_settings.html', context_instance=context)
