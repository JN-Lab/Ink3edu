from rest_framework import serializers

from .models import Student, Mentor, MentorsBuildingTrainings, StudentsFollowingTrainings

class StudentsFollowingTrainingsSerializer(serializers.ModelSerializer):
    """
    This serializer just formats all the information of the trainings associated to a student
    It is only used to build StudentSerializer
    """
    class Meta:
        model = StudentsFollowingTrainings
        fields = ('training', 'first_access', 'active', 'done')

class StudentSerializer(serializers.ModelSerializer):
    """
    This serializer is used to have the list of students with the trainings they are following
    """
    trainings = StudentsFollowingTrainingsSerializer(source='student_with_trainings', many=True, required=False)
    
    class Meta:
        model = Student
        fields = ('user', 'trainings')

class MentorsBuildingTrainingsSerializer(serializers.ModelSerializer):
    """
    This serializer just formats all the information of the trainings the mentors are working on.
    It is only used to build MentorSerializer
    """
    class Meta:
        model = MentorsBuildingTrainings
        fields = ('training', 'role')

class MentorSerializer(serializers.ModelSerializer):
    """
    This serializer is used to have the list of mentors with the trainings they are building
    """
    trainings = MentorsBuildingTrainingsSerializer(source='mentors_with_trainings', many=True, required=False)

    class Meta:
        model = Mentor
        fields = ('user', 'description', 'trainings')