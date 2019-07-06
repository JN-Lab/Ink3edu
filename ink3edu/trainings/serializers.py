from rest_framework import serializers

from .models import Training, Section, SectionsInTrainings, Chapter, ChaptersInSections


class ChapterSerializer(serializers.ModelSerializer):
    """
    This serializer just formats all the information of the chapter
    """
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'description')

class ChaptersInSectionsSerializer(serializers.ModelSerializer):
    """
    This serializer is used to build the SectionLongSerializer
    """
    class Meta:
        model = ChaptersInSections
        fields = ('id', 'chapter', 'chapter_number')

class SectionSimpleSerializer(serializers.ModelSerializer):
    """
    This serializer just formats the main information of the section
    without going further into the tree
    """
    class Meta:
        model = Section
        fields = ('id', 'title', 'description')

class SectionLongSerializer(serializers.ModelSerializer):
    """
    This serializer just formats all the information of the section
    until the chapter associated
    """
    chapters = ChaptersInSectionsSerializer(source='section_with_chapters', many=True, required=False)

    class Meta:
        model = Section
        fields = ('id', 'title', 'description', 'chapters')

class SectionsInTrainingsSerializer(serializers.ModelSerializer):
    """
    This serializer is used to build the TrainingLongSerializer
    """
    class Meta:
        model = SectionsInTrainings
        fields = ('id', 'section', 'section_number')

class TrainingSimpleSerializer(serializers.ModelSerializer):
    """
    This serializer just formats the main information of the training
    without going further into the tree
    """
    class Meta:
        model = Training
        fields = ('id' ,'title', 'description', 'status', 'price','category', 'mentors', 'students')

class TrainingLongSerializer(serializers.ModelSerializer):
    """
    This serializer just formats all the information of the training
    until the chapter associated
    """
    sections = SectionsInTrainingsSerializer(source='training_with_sections', many=True, required=False)

    class Meta:
        model = Training
        fields = ('id' ,'title', 'description', 'status', 'price','category','mentors', 'students', 'sections')