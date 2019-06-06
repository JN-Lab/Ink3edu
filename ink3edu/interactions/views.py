from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer