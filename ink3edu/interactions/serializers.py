from rest_framework import serializers

from .models import Student, Mentor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'trainings')

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('user', 'description', 'roles', 'trainings')