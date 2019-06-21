import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ink3edu.trainings.models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category

class TrainingDetailTest(APITestCase):
    """
    This class will test all the interactions we can have when we request a training
    """

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """
        TestDatabase.create()

    def test_get_one_training(self):
        python = Training.objects.get(title='python for beginner')
        url = reverse('trainings:training_detail', kwargs={'pk': python.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Temporary, just to be familiar with what we get as output
        response_str = json.dumps(response.data)
        look = json.loads(response_str)
        print(look)