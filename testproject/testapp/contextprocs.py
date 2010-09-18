from django.conf import settings


def settings_context_proc(request):
    return {'settings': settings}
