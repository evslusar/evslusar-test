from testapp.models import HttpRequestLog
from django.http import HttpRequest

class HttpRequestLogger:

     def process_request(self, request):
         if request.method == 'GET':
             method = 'G'
             params = request.GET.urlencode()
         elif request.method == 'POST':
             method = 'P'
             params = request.POST.urlencode()
         log_item = HttpRequestLog(path = request.path, method = method, request_dict = params)
         log_item.save()
