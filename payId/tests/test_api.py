import json
import unittest
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from ..models import LocalPayIdEntity
# from ..serializers import LocalPayIdEntitySerializer

client = Client()

class GetAllEntities(TestCase):

    def setUp(self):
        LocalPayIdEntity.objects.create(
            name='rockhoward')
        LocalPayIdEntity.objects.create(
            name='Yamood')
        entities = LocalPayIdEntity.objects.all()
        self.assertEqual(len(entities), 2)

    def test_get_PayIds(self):
        # Get API response for some test PayIds
        response = client.get('/Yamood/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        # print(str(data))
        self.assertEqual(data['payId'], 'yamood$payid.rockhoward.com')

        response = client.get('/rockhoward/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        # print(str(data))
        self.assertEqual(data['payId'], 'rockhoward$payid.rockhoward.com')

if __name__ == '__main__':
    unittest.main()
