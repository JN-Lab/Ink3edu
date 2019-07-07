from rest_framework import generics

from .models import Student, Mentor
from .serializers import StudentSerializer, MentorSerializer

class StudentList(generics.ListAPIView):
    """
    This view gets all the students information
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view gets all the info from one student
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MentorList(generics.ListAPIView):
    """
    This view gets all the mentors information
    """
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view gets all the info from one mentor
    """
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
