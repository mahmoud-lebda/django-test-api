from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='m@m.com',
            password='Test@123'
        )
        # allow us to login using django login auth
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='mahmoud@mahmoud.com',
            password='Test@123',
            name='test user'
        )

    def test_users_listed(self):
        """ test that users are listed in user page """
        # Reversing admin URLs
        # {{ app_label }}_{{ model_name }}_changelist
        url = reverse('admin:core_user_changelist')
        # performe a http to get the url
        res = self.client.get(url)
        # will check http is http 200 and the response contain a certain item
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ user edit page work """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        # status for http = 200 means ok
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ user add page work """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
