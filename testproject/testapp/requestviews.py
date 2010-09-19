from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from testapp.models import HttpRequestLog, RequestPriority
from testapp.forms import PriorityEditForm, requests


def paginate(objects, request):
    pagination = Paginator(objects, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        entries = pagination.page(page)
    except (EmptyPage, InvalidPage):
        entries = pagination.page(1)
    return entries


def request_log_view(request):
    entries = requests()
    entries_page = paginate(entries, request)
    args = {'entries': entries_page}
    return render_to_response('request_log_list.html', args,
        context_instance=RequestContext(request))


def edit_priority_view(request):
    if request.method == 'GET':
        edit_form = PriorityEditForm()
    elif request.method == 'POST':
        edit_form = PriorityEditForm(request.POST)
        edit_form.save_edition()
    args = {'edit_form': edit_form}
    return render_to_response('edit_priority.html', args,
        context_instance=RequestContext(request))
