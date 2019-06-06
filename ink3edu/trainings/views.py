from rest_framework import generics

from .models import Training
from .serializers import TrainingSerializer

class TrainingList(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer