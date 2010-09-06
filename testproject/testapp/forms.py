from django import forms
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

