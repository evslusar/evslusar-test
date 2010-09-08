from django.forms import TextInput
from django.conf import settings

class CalendarWidget(TextInput):
    class Media:
        css = {
            'all': (settings.SITE_MEDIA_PREFIX + 'css/ui-lightness/jquery-ui-1.8.4.custom.css',)
        }
        js = (settings.SITE_MEDIA_PREFIX + "js/jquery-1.4.2.min.js",
              settings.SITE_MEDIA_PREFIX + "js/jquery-ui-1.8.4.custom.min.js",
              settings.SITE_MEDIA_PREFIX + "js/datepicker.js",)

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'datepicker'})
