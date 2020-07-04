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

    def test_get_all_payIds(self):
        # Get API response for this unofficial endpoint
        response = client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], 'rockhoward$payid.rockhoward.com')
        self.assertEqual(data[1], 'yamood$payid.rockhoward.com')

if __name__ == '__main__':
    unittest.main()
