# Create your views here.

from testapp.models import *
from testapp.forms import PersonForm, AjaxPersonForm

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.http import HttpResponseForbidden, HttpResponseNotAllowed

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.conf import settings
from django.template import RequestContext

from django.core.paginator import Paginator, InvalidPage, EmptyPage



def default_person():
    return Person.objects.get(pk=1)

def default_person_info():
    p = default_person()
    info = { 'queryset': Person.objects.all(), 'object_id': p.pk, 'template_name': 'person_detail.html' }
    return info

def request_log_view(request):
    all_entries = HttpRequestLog.objects.all().order_by('-request_date')
    entries_paginator = Paginator(all_entries, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        entries = entries_paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = entries_paginator.page(1)
    return render_to_response('request_log_list.html', {'entries' : entries}, context_instance=RequestContext(request))




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
    return render_to_response('person_edit.html', {'form' : form}, context_instance=RequestContext(request))

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



def settings_context_proc(request):
    return {'settings': settings}

def settings_view(request):
    context = RequestContext(request, {}, [settings_context_proc])
    return render_to_response('view_settings.html', context_instance = context)











