from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating user with email"""
        email = 'test@gangawy.com'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normlizes(self):
        email = 'test@GANGAWY.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raisis error"""
        # any thing run here and don't rais error this test is fail
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test@123')

    def test_create_new_super_user(self):
        """ test creating new super user """
        user = get_user_model().objects.create_superuser(
            'm@ml.com',
            'Test@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
