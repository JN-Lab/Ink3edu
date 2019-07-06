from rest_framework import generics

from .models import Student, Mentor
from .serializers import StudentSerializer, MentorSerializer

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MentorList(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer