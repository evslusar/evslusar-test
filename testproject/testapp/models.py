from django.db import models
from django import forms

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    biography = models.TextField()


class PersonForm(forms.ModelForm):
    phone = forms.RegexField(regex='\d{7,10}', max_length=10, error_messages = {'invalid': 'Enter a valid phone number'})

    class Meta:
         model = Person
    


class HttpRequestLog(models.Model):

    request_method_choices = (
        ('G', 'GET'),
        ('P', 'POST'),
    )

    path = models.CharField(max_length=200)
    method = models.CharField(max_length=1, choices=request_method_choices)
    request_date = models.DateTimeField(auto_now_add=True)
    request_dict = models.TextField()

    def request_string(self):
        if self.method == 'G':
            method = 'GET'
        elif self.method == 'P':
            method = 'POST'
        return "%s %s" % (method, self.path,) 
