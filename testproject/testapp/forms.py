from django import forms
from django.conf import settings

from testapp.models import Person, RequestPriority, HttpRequestLog
from testapp.widgets import CalendarWidget


class PersonForm(forms.ModelForm):
    phone = forms.RegexField(regex='^\d{7,10}$',
        max_length=10,
        error_messages={'invalid': 'Enter a valid phone number'})
    birthdate = forms.DateField(widget=CalendarWidget())

    def as_p_with_submit(self):
        submit = '<input type="submit" value="Submit" />'
        return self.as_p() + submit

    class Meta:
        model = Person
        fields = ['birthdate', 'biography', 'phone',
            'email', 'lastname', 'firstname']


media_prefix = '/' + settings.STATIC_MEDIA_PREFIX


class AjaxPersonForm(PersonForm):

    class Media:
        js = (media_prefix + "js/jquery-1.4.2.min.js",
            media_prefix + "js/jquery-form-2.4.7.js",
            media_prefix + "js/edit_ajax.js",)


def priorities():
    return RequestPriority.objects.all()


def requests():
    query = HttpRequestLog.objects.all()
    query = query.order_by('-request_date')
    query = query.order_by('priority__value')
    return query


class PriorityEditForm(forms.Form):

    priority = forms.ModelChoiceField(required=True,
        queryset=priorities(),
        error_messages={'required': 'Select a priority'})
    requests = forms.ModelMultipleChoiceField(required=True,
        queryset=requests(),
        error_messages={'required': 'Select at least one request'})

    def save_edition(self):
        if self.is_bound and self.is_valid():
            new_priority = self.cleaned_data['priority']
            updated_requests = self.cleaned_data['requests']
            updated_requests.update(priority=new_priority)
