import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ink3edu.trainings.models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category

class ChapterTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """
        TestDatabase.create()

    def test_get_all_chapters_info_not_connected(self):
        url = reverse('trainings:chapters_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_one_chapter_info_not_connected(self):
        computer_birth = Chapter.objects.get(title='the birth of computer')
        url = reverse('trainings:chapter_detail', kwargs={'pk': computer_birth.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)