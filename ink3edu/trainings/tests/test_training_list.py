import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ink3edu.trainings.models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category

class TrainingListTest(APITestCase):
    """
    This class will test all the interactions we can have with a list of Trainings.
    What will be tested:
        (PHASE 1 : no permissions)
        -> Get all the trainings
    """

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """
        TestDatabase.create()

    def test_get_all_trainings(self):
        url = reverse('trainings:trainings_list')
        response = self.client.get(url, format='json')
        trainings = Training.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), trainings)
        
        # Temporary, just to be familiar with what we get as output
        response_str = json.dumps(response.data)
        look = json.loads(response_str)
        print(look)