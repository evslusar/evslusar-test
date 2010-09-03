

from django.test import TestCase

from testapp.models import Person
from testapp.views import default_person_info
from testapp.views import default_person

from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict
from testapp.models import HttpRequestLog

from django.contrib.auth.models import User


class PersonModelTest(TestCase):

    def test_initial_data(self):

        # test initial data loaded
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

        default_person = info['queryset'].get(pk = info['object_id'])
        self.assertEqual(default_person.firstname, "Evgeniy")
        self.assertEqual(default_person.lastname, "Slusar")


class HttpRequestLogTest(TestCase):


    def get_log_item(self, path):
        return HttpRequestLog.objects.get(path__iexact = path)

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


class PersonEditTest(TestCase):

    def test_person_edit(self):

        test_name = 'test'
        test_paswd = 'password'
        test_email = 'test@mail.com'
 
        user = User.objects.create_user(test_name, test_email, test_paswd)
        user.save()
        self.assertTrue(user.check_password(test_paswd))
        self.client.post('/login/', {'username': test_name, 'password': test_paswd})

        params = { 'firstname': 'Evgeniy', 'lastname': 'Slusar', 'email': 'abs@gmail.com', 'phone': '0000000000', 'biography': 'bio' }

        self.client.post('/edit/', params)
        dp = default_person()
        self.assertEqual(dp.firstname, params['firstname'])
        self.assertEqual(dp.lastname, params['lastname'])
        self.assertEqual(dp.email, params['email'])
        self.assertEqual(dp.phone, params['phone'])
        self.assertEqual(dp.biography, params['biography'])



from django.conf import settings

class ContextProcTest(TestCase):

    def test_context_proc(self):    
        response = self.client.get('/settings/')
        context_settings = response.context['settings']
        self.assertEqual(settings, context_settings)



















        

