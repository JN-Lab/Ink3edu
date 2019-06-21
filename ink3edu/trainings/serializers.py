from rest_framework import serializers

from .models import Training, Section, SectionsInTrainings

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('id', 'title', 'description')

class SectionsInTrainingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SectionsInTrainings
        fields = ('id', 'section', 'section_number')

class TrainingSerializer(serializers.ModelSerializer):

    sections = SectionsInTrainingsSerializer(source='training_with_sections', many=True, required=False)

    class Meta:
        model = Training
        fields = ('id' ,'title', 'description', 'status', 'price','category', 'sections')