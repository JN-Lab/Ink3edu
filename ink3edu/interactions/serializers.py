from rest_framework import serializers

from .models import Student, Mentor, MentorsBuildingTrainings, StudentsFollowingTrainings

class StudentsFollowingTrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsFollowingTrainings
        fields = ('training', 'first_access', 'active', 'done')

class StudentSerializer(serializers.ModelSerializer):
    trainings = StudentsFollowingTrainingsSerializer(source='student_with_trainings', many=True, required=False)
    
    class Meta:
        model = Student
        fields = ('user', 'trainings')

class MentorsBuildingTrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorsBuildingTrainings
        fields = ('training', 'role')

class MentorSerializer(serializers.ModelSerializer):
    trainings = MentorsBuildingTrainingsSerializer(source='mentors_with_trainings', many=True, required=False)

    class Meta:
        model = Mentor
        fields = ('user', 'description', 'trainings')