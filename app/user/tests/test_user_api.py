from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# import rest framework test helper tools
# test client to make request to our api
# and check what is the response
from rest_framework.test import APIClient
# D
from rest_framework import status


# constant for url
CREATE_USER_URL = reverse('user:create')


# helper function that will create user
# and use it every time when we need user
def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PuplicUserApiTests(TestCase):
    """ test any puplic api """

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """ test creating user with valid payload """
        payload = {
            'email': 'test@test.com',
            'password': 'Test@123',
            'name': 'ali'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # unwind the dic response with data it looks like
        # payload but wit id
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_usrs_exists(self):
        """test creating a user that already exist """
        payload = {
            'email': 'test@test.com',
            'password': 'Test@123',
            'name': 'mahmoud'
            }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """ test if password too short """
        payload = {
            'email': 'mahmoud@mahmou.com',
            'password': 'pw',
            'name': 'mahmoud'
             }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
