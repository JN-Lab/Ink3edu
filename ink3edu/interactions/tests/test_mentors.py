import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ink3edu.interactions.models import Mentor

class MentorTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """        
        TestDatabase.create()

    def test_get_all_mentors_info(self):
        url = reverse('interactions:mentors_list')
        response = self.client.get(url, format='json')
        mentors = Mentor.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), mentors)

         # Temporary, just to be familiar with what we get as output
        response_str = json.dumps(response.data)
        look = json.loads(response_str)
        print(look)   