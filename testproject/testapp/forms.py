from django import forms
from django.conf import settings

from testapp.models import Person, RequestPriority
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


def make_priority_choices():
    all_priors = RequestPriority.objects.all()
    vals = [prior.value for prior in all_priors]
    names = ['Priority #%d' % val for val in vals]
    choices = zip(vals, names)
    return choices


class SelectForm(forms.Form):
    select = forms.ChoiceField(make_priority_choices())
