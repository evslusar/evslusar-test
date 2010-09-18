from django.forms import TextInput
from django.conf import settings


media_prefix = '/' + settings.STATIC_MEDIA_PREFIX
jquery_ui = 'css/ui-lightness/jquery-ui-1.8.4.custom.css'


class CalendarWidget(TextInput):
    class Media:
        css = {
            'all': (media_prefix + jquery_ui,)}
        js = (media_prefix + "js/jquery-1.4.2.min.js",
              media_prefix + "js/jquery-ui-1.8.4.custom.min.js",
              media_prefix + "js/datepicker.js",)

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'datepicker'})
