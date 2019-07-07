import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ink3edu.interactions.models import Student

class StudentTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """
        We create a database to realize the different tests of the class
        """        
        TestDatabase.create()

    def test_get_all_students_info(self):
        url = reverse('interactions:students_list')
        response = self.client.get(url, format='json')
        students = Student.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), students)

        # Temporary, just to be familiar with what we get as output
        response_str = json.dumps(response.data)
        look = json.loads(response_str)
        print(look)

    def test_get_one_student_info(self):
        john = User.objects.get(username='john')
        john_student = Student.objects.get(user=john)
        url = reverse('interactions:student_detail', kwargs={'pk': john_student.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Temporary, just to be familiar with what we get as output
        response_str = json.dumps(response.data)
        look = json.loads(response_str)
        print(look)