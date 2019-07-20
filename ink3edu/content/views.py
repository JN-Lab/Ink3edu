from rest_framework import generics

from .models import Content
from .serializers import ContentSerializer

class ContentList(generics.ListAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer