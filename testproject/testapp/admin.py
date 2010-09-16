from django.contrib import admin

from testapp.models import Person
from testapp.models import HttpRequestLog


class PersonAdmin(admin.ModelAdmin):
    pass


class HttpRequestLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(HttpRequestLog, HttpRequestLogAdmin)
