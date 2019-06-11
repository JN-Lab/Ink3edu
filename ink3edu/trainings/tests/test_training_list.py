from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ink3edu.helper_dbtestdata import TestDatabase
from ink3edu.users.models import User
from ..models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category