# Create your views here.

from testapp.models import Person

def default_person_info():
    default_person = Person.objects.get(firstname__iexact = 'Evgeniy', lastname__iexact = 'Slusar')
    info = { 'queryset': Person.objects.all(), 'object_id': default_person.pk, 'template_name': 'person_detail.html' }
    return info

