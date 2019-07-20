from rest_framework import serializers

from .models import Content, ContentsInChapters

class ContentsInChaptersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentsInChapters
        fields = ('chapter', 'content_number')

class ContentSerializer(serializers.ModelSerializer):

    chapters = ContentsInChaptersSerializer(source='content_per_chapters', many=True, required=False)

    class Meta:
        model = Content
        fields = ('title', 'description', 'mentor', 'groups', 'url_content_readonly', 'url_content_modification_allowed', 'chapters')