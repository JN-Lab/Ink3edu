#! /usr/bin/env python3
# coding: utf-8
from .users.models import User
from .trainings.models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections, Status, Category
from .interactions.models import Student, Mentor, Role, Group, StudentsFollowingTrainings, MentorsBuildingTrainings

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
        We create some groups for the mentors:
            - grp_a
            - grp_b
        We associate the mentors in some groups:
            - grp_a :
                - mentor_lee
                - mentor_george
                - mentor_admin
            - grp_b :
                - mentor_admin
                - mentor_brandon
                - mentor_mike
        """

        # We create groups grp_a and grp_b
        grp_a = Group.objects.create(name='grp_a', description="this is group A")
        grp_b = Group.objects.create(name='grp_b', description="this is group B")

        # We associate the mentors to the adequate groups
        grp_a.mentors.add(mentor_lee, mentor_george, mentor_admin)
        grp_b.mentors.add(mentor_admin, mentor_brandon, mentor_mike)

        """
        We create some roles for mentors:
            - owner
            - contributor
        """

        owner = Role.objects.create(label='owner', description='this is the owner of the training')
        contributor = Role.objects.create(label='contributor', description='this is one of the contributor of the training')

        """
        We create the two status which are used for each training.
        We have two choices:
            - public
            - private
        """
        public = Status.objects.create(name=Status.PUBLIC)
        private = Status.objects.create(name=Status.PRIVATE)

        """
        We create the categories which will be associated to each training:
            - development
            - data
            - cloud
        """

        development = Category.objects.create(name='development')
        data = Category.objects.create(name='data')
        cloud = Category.objects.create(name='cloud')

        """
        We create the trainings:
            - python
            - aws
            - docker
        We associate directly the training with the status and category
        """

        python = Training.objects.create(title='python for beginner',
                                         description='this is a course to start coding in Python',
                                         price=0.00,
                                         status=public,
                                         category=development)

        aws = Training.objects.create(title='Amazon Web Services for beginner',
                                      description='learn the basics of Amazon Web Services',
                                      price=59.99,
                                      status=private,
                                      category=cloud)

        docker = Training.objects.create(title='Introduction to Docker',
                                      description='Discover the universe of container by learning Docker',
                                      price=24.99,
                                      status=private,
                                      category=cloud)

        """
        We associate some students to these trainings:
            - student_john subscribes to python training
            - student_paul subscribes to python and aws trainings
            - student_george subscribes to docker training
            - student_mike subscribes to aws and docker trainings
        """

        student_john_follows_python_training = StudentsFollowingTrainings.objects.create(student=student_john,
                                                                                         training=python)

        student_paul_follows_python_training = StudentsFollowingTrainings.objects.create(student=student_paul,
                                                                                         training=python)

        student_paul_follows_aws_training = StudentsFollowingTrainings.objects.create(student=student_paul,
                                                                                         training=aws)

        student_george_follows_docker_training = StudentsFollowingTrainings.objects.create(student=student_george,
                                                                                         training=docker)

        student_mike_follows_aws_training = StudentsFollowingTrainings.objects.create(student=student_mike,
                                                                                         training=aws)

        student_mike_follows_docker_training = StudentsFollowingTrainings.objects.create(student=student_mike,
                                                                                         training=docker)



        """
        We associate some mentors to these trainings:
            - mentor_admin is the owner of python training and one contributor of aws training
            - mentor_lee is the owner of aws training
            - mentor_brandon is a contributor of python and aws training
            - mentor_george is the owner of docker training
            - mentor_mike is a contributor of aws and docker trainings
        """

        mentor_admin_builds_python_training = MentorsBuildingTrainings.objects.create(mentor=mentor_admin,
                                                                                      training=python,
                                                                                      role=owner)

        mentor_admin_contributes_aws_training = MentorsBuildingTrainings.objects.create(mentor=mentor_admin,
                                                                                        training=aws,
                                                                                        role=contributor)

        mentor_lee_builds_aws_training = MentorsBuildingTrainings.objects.create(mentor=mentor_lee,
                                                                                 training=aws,
                                                                                 role=owner)

        mentor_brandon_contributes_python_training = MentorsBuildingTrainings.objects.create(mentor=mentor_brandon,
                                                                                             training=python,
                                                                                             role=contributor)

        mentor_brandon_contributes_aws_training = MentorsBuildingTrainings.objects.create(mentor=mentor_brandon,
                                                                                          training=aws,
                                                                                          role=contributor)

        mentor_george_builds_docker_training = MentorsBuildingTrainings.objects.create(mentor=mentor_george,
                                                                                       training=docker,
                                                                                       role=owner)

        mentor_mike_contributes_aws_training = MentorsBuildingTrainings.objects.create(mentor=mentor_mike,
                                                                                       training=aws,
                                                                                       role=contributor)

        mentor_mike_contributes_docker_training = MentorsBuildingTrainings.objects.create(mentor=mentor_mike,
                                                                                          training=docker,
                                                                                          role=contributor)

        """
        We create some sections:
            - the section programming_story
            - the section server_role
        """

        programming_story = Section.objects.create(title='the history of programming',
                                                   description='what is the history of programming')

        server_role = Section.objects.create(title='what a server can do?',
                                             description='a server can do a lot of things, even burning')


        """
        We associate these sections to the existing trainings:
            - the section programming_story is the first section of python training
            - the section programming_story is the first section of docker training
            - the section server_role is the first section of aws training
            - the section server_role is the second section of docker training
        """

        programming_story_in_python_training = SectionsInTrainings.objects.create(training=python,
                                                                                  section=programming_story,
                                                                                  section_number=1)

        programming_story_in_docker_training = SectionsInTrainings.objects.create(training=docker,
                                                                                  section=programming_story,
                                                                                  section_number=1)

        server_role_in_aws_training = SectionsInTrainings.objects.create(training=aws,
                                                                         section=server_role,
                                                                         section_number=1)

        server_role_in_docker_training = SectionsInTrainings.objects.create(training=docker,
                                                                            section=server_role,
                                                                            section_number=2)

        """
        We create some chapters:
            - chapter computer_birth
            - chapter first_language
            - chapter server_computer
        """

        computer_birth = Chapter.objects.create(title='the birth of computer',
                                                description='one upon a time... A computer is born.')

        first_language = Chapter.objects.create(title='a computer can listen',
                                                description='you can talk with a computer, and it is quite funny.')

        server_computer = Chapter.objects.create(title='a chapter with no interest',
                                                 description='a server is a computer but... Is a computer a server?')

        """
        We associate these chapters to the existing sections:
            - the chapter computer_birth is the first chapter of programming_story section
            - the chapter computer_birth is the second chapter of server_role section
            - the chapter first_language is the second chapter of programming_story section
            - the chapter server_computer is the first chapter of server_role section
        """

        computer_birth_in_programming_story = ChaptersInSections.objects.create(section=programming_story,
                                                                                chapter=computer_birth,
                                                                                chapter_number=1)

        computer_birth_in_server_role = ChaptersInSections.objects.create(section=server_role,
                                                                          chapter=computer_birth,
                                                                          chapter_number=2)

        first_language_in_programming_story = ChaptersInSections.objects.create(section=programming_story,
                                                                                chapter=first_language,
                                                                                chapter_number=2)

        server_computer_in_server_role = ChaptersInSections.objects.create(section=server_role,
                                                                           chapter=server_computer,
                                                                           chapter_number=1)
