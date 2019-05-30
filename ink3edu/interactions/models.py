from django.db import models
from django.utils import timezone
from ink3edu.users.models import User
from ink3edu.trainings.models import Training

class Student(models.Model):
    """
    This class represents the students created
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainings = models.ManyToManyField(Training,
                                       through='StudentsFollowingTrainings',
                                       related_name='students')

    def __str__(self):
        return "{} - {} - {}".format(self.user.username, self.user.first_name, self.user.last_name)

class Mentor(models.Model):
    """
    This class represents the mentors created
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    trainings = models.ManyToManyField(Training,
                                       through='MentorsBuildingTrainings',
                                       related_name='mentors')
    roles = models.ManyToManyField('Role',
                                    through='MentorsBuildingTrainings',
                                    related_name='mentors')

    def __str__(self):
        return "{} - {} - {}".format(self.user.username, self.user.first_name, self.user.last_name)

class Role(models.Model):
    """
    This class represents the roles created
    """
    label = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.label

class Group(models.Model):
    """
    This class represents the groups created
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    mentors = models.ManyToManyField('Mentor',
                                     related_name='groups')

    def __str__(self):
        return self.name

class StudentsFollowingTrainings(models.Model):
    """
    This class represents the students per trainings
    This is an association table between Student and Training
    """
    student = models.ForeignKey('Student',
                                on_delete=models.CASCADE,
                                related_name='student_with_trainings')
    training = models.ForeignKey(Training,
                                 on_delete=models.CASCADE,
                                 related_name='training_per_student')
    done = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    first_access = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} -{}".format(self.student.user.username, self.training.title)

class MentorsBuildingTrainings(models.Model):
    """
    This class represents the mentors per trainings with their roles
    This is an association table between Student, Training and Role
    """
    mentor = models.ForeignKey('Mentor',
                               on_delete=models.CASCADE,
                               related_name='mentors_with_trainings')
    training = models.ForeignKey(Training,
                                 on_delete=models.CASCADE,
                                 related_name='training_per_mentors')

    role = models.ForeignKey('Role',
                             on_delete=models.CASCADE,
                             related_name='role_per_mentors')

    def __str__(self):
        return "{} - {} - {}".format(self.mentor.user.username, self.training.title, self.role.label)