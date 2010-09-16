from datetime import date

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict
from django.contrib.auth.models import User
from django.conf import settings

from testapp.models import Person, HttpRequestLog
from testapp.views import default_person_info, default_person


class PersonModelTest(TestCase):

    def test_initial_data(self):
        person = default_person()
        self.assertTrue(person)
        self.assertEqual(person.firstname, "Evgeniy")
        self.assertEqual(person.lastname, "Slusar")


class DefaultPersonInfoTest(TestCase):

    def test_default_person(self):
        info = default_person_info()
        self.assertTrue(info)
        self.assertEqual(info['object_id'], 1)
        self.assertEqual(info['template_name'], "person_detail.html")
        self.assertTrue(info['queryset'])

        default_person = info['queryset'].get(pk=info['object_id'])
        self.assertEqual(default_person.firstname, "Evgeniy")
        self.assertEqual(default_person.lastname, "Slusar")


class HttpRequestLogTest(TestCase):

    def get_log_item(self, path):
        return HttpRequestLog.objects.get(path__iexact=path)

    def test_request_log(self):
        test_path = '/'
        test_params = 'a=1&b=2'
        self.client.get('%s?%s' % (test_path, test_params,))

        try:
            log_item = self.get_log_item(test_path)
        except ObjectDoesNotExist:
            self.assertTrue(False, "Request not saved")
        self.assertEqual(log_item.path, test_path)
        self.assertEqual(log_item.method, 'G')
        params = QueryDict(log_item.request_dict)
        self.assertEqual(params['a'], '1')
        self.assertEqual(params['b'], '2')


def remove_csrf_middleware():
    csrf_middleware = 'django.contrib.csrf.middleware.CsrfMiddleware'
    middlewares = settings.MIDDLEWARE_CLASSES
    if csrf_middleware in middlewares:
        middlewares.remove(csrf_middleware)


class AuthTest(TestCase):

    def setUp(self):
        test_name = 'test'
        test_paswd = 'password'
        test_email = 'test@mail.com'

        user = User.objects.create_user(test_name, test_email, test_paswd)
        user.save()

        remove_csrf_middleware()
        self.client.post('/login/', {'username': test_name,
            'password': test_paswd})


class PersonEditTest(AuthTest):

    def test_person_edit(self):
        params = {'firstname': 'Evgeniy',
            'lastname': 'Slusar',
            'email': 'abs@gmail.com',
            'phone': '0000000000',
            'biography': 'bio',
            'birthdate': date(2010, 1, 1)}

        self.client.post('/edit/', params)
        dp = default_person()
        self.assertEqual(dp.firstname, params['firstname'])
        self.assertEqual(dp.lastname, params['lastname'])
        self.assertEqual(dp.email, params['email'])
        self.assertEqual(dp.phone, params['phone'])
        self.assertEqual(dp.biography, params['biography'])
        self.assertEqual(dp.birthdate, params['birthdate'])


class ContextProcTest(TestCase):

    def test_context_proc(self):
        response = self.client.get('/settings/')
        context_settings = response.context['settings']
        self.assertEqual(settings, context_settings)


class CalendarTest(AuthTest):

    def test_calendar_widget(self):
        css_link = '<link href="/' \
            + settings.STATIC_MEDIA_PREFIX \
            + 'css/%s" type="text/css" media="%s" rel="stylesheet" />'
        css_files = ({'file': 'ui-lightness/jquery-ui-1.8.4.custom.css',
            'media': 'all'},)
        js_link = '<script type="text/javascript" src="/' \
            + settings.STATIC_MEDIA_PREFIX \
            + 'js/%s"></script>'
        js_files = ('jquery-1.4.2.min.js',
            'jquery-ui-1.8.4.custom.min.js',
            'datepicker.js',)

        response = self.client.get('/edit/')
        for js_file in js_files:
            self.assertContains(response, js_link % js_file)
        for css_file in css_files:
            self.assertContains(response, css_link % (css_file['file'],
                css_file['media'],))


class FieldsReverseOrderTest(AuthTest):

    def test_fields_reverse_order(self):
        response = self.client.get('/edit/')
        form = response.context['form']
        fields_order = [field.name for field in form]
        test_order = ['birthdate', 'biography', 'phone',
            'email', 'lastname', 'firstname']
        for pair in zip(fields_order, test_order):
            self.assertEqual(pair[0], pair[1])
