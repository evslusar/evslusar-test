# Create your views here.

from testapp.models import *
from testapp.forms import PersonForm

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.conf import settings
from django.template import RequestContext


def default_person():
    return Person.objects.get(pk=1)

def default_person_info():
    p = default_person()
    info = { 'queryset': Person.objects.all(), 'object_id': p.pk, 'template_name': 'person_detail.html' }
    return info


def request_log_info():
    return { 'queryset': HttpRequestLog.objects.all().order_by('-request_date'), 'template_name': 'request_log_list.html' }





@login_required
def edit_view(request):
    form = PersonForm()
    if request.method == 'GET':
        form = PersonForm(instance=default_person())
    elif request.method == 'POST':
        form = PersonForm(request.POST, instance=default_person())
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/')
    return render_to_response('person_edit.html', {'form' : form}, context_instance=RequestContext(request))



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def settings_context_proc(request):
    return {'settings': settings}

def settings_view(request):
    context = RequestContext(request, {}, [settings_context_proc])
    return render_to_response('view_settings.html', context_instance = context)











