import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ink3edu.trainings.models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category

class TrainingListTest(APITestCase):
    """
    This class tests all the interactions we can have with a list of Trainings.
    What will be tested:
        -> Not Connected:
            FAIL:
                -> Get all trainings
                -> Get one specific training

        -> With admin account:
            SUCCESS:
                -> Get all trainings with all the information of the tree until the chapters
                -> Get all trainings without all the information of the tree
                -> Get one specific training with all the information of the tree until the chapters
                -> Get one specific without all the information of the tree
                -> Create a new training (only direct training information = model field)
                -> Update a training (only direct training information = model field)
                -> Delete a training (only direct training information = model field)
            FAIL:
                -> Update a section linked to a selected training (read-only)
                -> Update a chapter linked to a section linked to a selected training (read-only)

        -> With mentor access
            SUCCESS:
                -> Get all trainings with all the information of the tree until the chapters
                -> Get all trainings without all the information of the tree
                -> Get one specific training with all the information of the tree until the chapters
                -> Get one specific without all the information of the tree
                -> Create a new training (only direct training information = model field)
                -> Update a training (only direct training information = model field) only if request.user == mentor 
                -> Delete a training (only direct training information = model field) only if request.user == mentor
            FAIL:
                -> Update a section linked to a selected training (read-only)
                -> Update a chapter linked to a section linked to a selected training (read-only)
                -> Update a training (only direct training information = model field) only if request.user != mentor 
                -> Delete a training (only direct training information = model field) only if request.user != mentor
        
        -> With student access
            SUCCESS:
                -> Get all trainings with all the information of the tree until the chapters
                -> Get all trainings without all the information of the tree
                -> Get one specific training with all the information of the tree until the chapters
                -> Get one specific without all the information of the tree
            FAIL:
                -> Create a new training (only direct training information = model field)
                -> Update a training (only direct training information = model field)
                -> Delete a training (only direct training information = model field)
    """

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """
        TestDatabase.create()

    def test_get_all_trainings_simple_info(self):
        """
        This test checks:

        """
        url = reverse('trainings:trainings_simple_list')
        response = self.client.get(url, format='json')
        trainings = Training.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), trainings)
        
        # Temporary, just to be familiar with what we get as output
        response_str = json.dumps(response.data)
        look = json.loads(response_str)
        print(look)

    def test_get_all_trainings_long_info(self):
        url = reverse('trainings:trainings_long_list')
        response = self.client.get(url, format='json')
        trainings = Training.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), trainings)
        
        # Temporary, just to be familiar with what we get as output
        response_str = json.dumps(response.data)
        look = json.loads(response_str)
        print(look)

class SectionListTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """
        TestDatabase.create()

    def test_get_all_sections_simple_info(self):
        url = reverse('trainings:sections_simple_list')
        response = self.client.get(url, format='json')
        sections = Section.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), sections)

    def test_get_all_sections_long_info(self):
        url = reverse('trainings:sections_long_list')
        response = self.client.get(url, format='json')
        sections = Section.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), sections)

class ChapterListTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """
        TestDatabase.create()

    def test_get_all_chapters_info(self):
        url = reverse('trainings:chapters_list')
        response = self.client.get(url, format='json')
        chapters = Chapter.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), chapters)