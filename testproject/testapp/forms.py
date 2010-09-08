from django import forms
from django.conf import settings
from django.forms.util import ErrorList
from testapp.models import Person
from testapp.widgets import CalendarWidget


class PersonForm(forms.ModelForm):
    phone = forms.RegexField(regex='^\d{7,10}$', max_length=10, error_messages = {'invalid': 'Enter a valid phone number'})
    birthdate = forms.DateField(widget=CalendarWidget())
                
    class Meta:
        model = Person
        fields = ['birthdate', 'biography', 'phone', 'email', 'lastname', 'firstname']
#         fields = [x for x in reversed([field.name for field in PersonForm])]

    def as_p_with_submit(self):
        submit = '<input type="submit" value="Submit" />'
        return self.as_p() + submit


class AjaxPersonForm(PersonForm):
    class Media:
        js = (settings.SITE_MEDIA_PREFIX + "js/jquery-1.4.2.min.js",
              settings.SITE_MEDIA_PREFIX + "js/jquery-form-2.4.7.js",
              settings.SITE_MEDIA_PREFIX + "js/edit_ajax.js",)

