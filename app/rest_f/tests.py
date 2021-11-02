from django.http import response
from django.test import TestCase

from rest_framework.test import APITestCase, RequestsClient

# Create your tests here.


class API_Testing(APITestCase):

    def test_post_address(self):
        test_data = {
            'city': 'Rivne'
        }
        response = self.client.get(
            'http://127.0.0.1:8000/address/', data=test_data)

        print(response.json(), response.status_code)
        self.assertEqual(response.status_code, 201)
