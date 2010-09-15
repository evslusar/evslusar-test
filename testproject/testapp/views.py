from testapp.models import Person, HttpRequestLog


def default_person_info():
    default_person = Person.objects.get(firstname__iexact='Evgeniy',
        lastname__iexact='Slusar')
    info = {'queryset': Person.objects.all(),
        'object_id': default_person.pk,
        'template_name': 'person_detail.html'}
    return info


def request_log_info():
    all_requests = HttpRequestLog.objects.all()
    return {'queryset': all_requests.order_by('-request_date'),
        'template_name': 'request_log_list.html'}
