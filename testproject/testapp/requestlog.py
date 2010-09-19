from django.http import HttpRequest

from testapp.models import HttpRequestLog, RequestPriority


class HttpRequestLogger:

    def priority(self, request):
        prior = RequestPriority.objects.get(value__exact=1)
        return prior

    def process_request(self, request):
        if request.method == 'GET':
            method = 'G'
            params = request.GET.urlencode()
        elif request.method == 'POST':
            method = 'P'
            params = request.POST.urlencode()
        log_item = HttpRequestLog(path=request.path,
            method=method, request_dict=params)
        log_item.priority = self.priority(request)
        log_item.save()
