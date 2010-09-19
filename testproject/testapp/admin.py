from django.contrib import admin

from testapp.models import Person
from testapp.models import HttpRequestLog, RequestPriority


class PersonAdmin(admin.ModelAdmin):
    pass


class HttpRequestLogAdmin(admin.ModelAdmin):
    pass


class RequestPriorityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(HttpRequestLog, HttpRequestLogAdmin)
admin.site.register(RequestPriority, RequestPriorityAdmin)
