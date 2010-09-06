from django import forms
from testapp.models import Person
from testapp.widgets import CalendarWidget


class PersonForm(forms.ModelForm):
    phone = forms.RegexField(regex='^\d{7,10}$', max_length=10, error_messages = {'invalid': 'Enter a valid phone number'})
    birthdate = forms.DateField(widget=CalendarWidget())

    class Meta:
         model = Person
