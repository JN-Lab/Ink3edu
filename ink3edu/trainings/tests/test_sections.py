import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ink3edu.trainings.models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category

class SectionTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """
        TestDatabase.create()

    def test_get_all_sections_simple_info_not_connected(self):
        url = reverse('trainings:sections_simple_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_sections_long_info_not_connected(self):
        url = reverse('trainings:sections_long_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_section_simple_info_not_connected(self):
        programming_story = Section.objects.get(title='the history of programming')
        url = reverse('trainings:section_simple_detail', kwargs={'pk': programming_story.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_section_long_info_not_connected(self):
        programming_story = Section.objects.get(title='the history of programming')
        url = reverse('trainings:section_long_detail', kwargs={'pk': programming_story.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)