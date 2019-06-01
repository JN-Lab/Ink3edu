#! /usr/bin/env python3
# coding: utf-8
from users.models import User
from trainings.models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category
from interactions.models import Student, Mentor, Role, Group, StudentsFollowingTrainings, MentorsBuildingTrainings

class TestDatabase:
    """
    This presents a dataset which has to be used for all unit tests. 
    """

    @staticmethod
    def create():
        """
        This method creates the dataset for the unit tests
        """
        
        """
        We create some users with different typologies:
            - We create an admin account which is also a mentor
            - We create john and paul which are students
            - We create lee and brandon which are mentors
            - We create mike and mike which are students and mentors
        """

        # We create an admin account which is also a mentor
        admin = User.objects.create_superuser(username='admin_user', password='admin_password', email='test@test.com')
        mentor_admin = Mentor(user=admin)
        mentor_admin.save()
        
        # We create john which is a student (student_john)
        john = User.objects.create_user(username='john', password='john_password', is_staff=False)
        student_john = Student(user=john)
        student_john.save()

        # We create john which is a student (student_john)
        paul = User.objects.create_user(username='paul', password='paul_password', is_staff=False)
        student_paul = Student(user=paul)
        student_paul.save()

        # We create lee which is a mentor (mentor_lee)
        lee = User.objects.create_user(username='lee', password='lee_password')
        mentor_lee = Mentor(user=lee)
        mentor_lee.save()

        # We create brandon which is a mentor (mentor_brandon)
        brandon = User.objects.create_user(username='brandon', password='brandon_password')
        mentor_brandon = Mentor(user=brandon)
        mentor_brandon.save()

        # We create george which is a student (student_george) and a mentor (mentor_george)
        george = User.objects.create_user(username='george', password='george_password')
        student_george = Student(user=george)
        student_george.save()
        mentor_george = Mentor(user=george)
        mentor_george.save()

        # We create mike which is a student (student_mike) and a mentor (mentor_mike) 
        mike = User.objects.create_user(username='mike', password='mike_password')
        student_mike = Student(user=mike)
        student_mike.save()
        mentor_mike = Mentor(user=mike)
        mentor_mike.save()

        """
        We create some roles for mentors:
            - 
            - 
        We will associate these roles to the different mentors:
            - 
            - 
        """
        # We create role

        # We create groups

        # We create trainings

        # We create Sections

        # We create Chapters