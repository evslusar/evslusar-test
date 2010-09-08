from testapp.models import HttpRequestLog, RequestPriority
from django.http import HttpRequest

class HttpRequestLogger:
    def priority(self, request):
        try:
            val = int(request.REQUEST['prior'])
        except:
            val = 1
        if val <= 0:
            val = 1
        try:
            prior = RequestPriority.objects.get(value__exact=val)
        except:
            prior = RequestPriority.objects.get(value__exact=1)
        return prior

    def process_request(self, request):
        if request.method == 'GET':
            method = 'G'
            params = request.GET.urlencode()
        elif request.method == 'POST':
            method = 'P'
            params = request.POST.urlencode()
        log_item = HttpRequestLog(path = request.path, method = method, request_dict = params)
        log_item.priority = self.priority(request)
        log_item.save()
