from rest_framework import generics

from .models import Training, Section, Chapter
from .serializers import TrainingLongSerializer, TrainingSimpleSerializer, SectionLongSerializer, SectionSimpleSerializer, ChapterSerializer

class ChapterList(generics.ListCreateAPIView):
    """
    This view gets all the chapters information
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view gets all the info from one chapter
    """    
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class SectionSimpleList(generics.ListCreateAPIView):
    """
    This view gets all the sections without going further than training info
    """
    queryset = Section.objects.all()
    serializer_class = SectionSimpleSerializer

class SectionLongList(generics.ListCreateAPIView):
    """
    This view gets all the sections with all the tree until chapters
    """
    queryset = Section.objects.all()
    serializer_class = SectionLongSerializer

class SectionSimpleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to get one section without going further than training info
    """
    queryset = Section.objects.all()
    serializer_class = SectionSimpleSerializer

class SectionLongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to get one section with all the tree information until chapters
    """
    queryset = Section.objects.all()
    serializer_class = SectionLongSerializer

class TrainingSimpleList(generics.ListCreateAPIView):
    """
    This view gets all the trainings without going further than training info
    """
    queryset = Training.objects.all()
    serializer_class = TrainingSimpleSerializer

class TrainingLongList(generics.ListCreateAPIView):
    """
    This view gets all the trainings with all the tree until chapters
    """
    queryset = Training.objects.all()
    serializer_class = TrainingLongSerializer

class TrainingSimpleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to get one training without going further than training info
    """
    queryset = Training.objects.all()
    serializer_class = TrainingSimpleSerializer

class TrainingLongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to get one training with all the tree information until chapters
    """
    queryset = Training.objects.all()
    serializer_class = TrainingLongSerializer