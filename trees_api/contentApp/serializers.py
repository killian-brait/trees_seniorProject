# serializers.py 
# Purpose: Serializers for the User App (turn models into JSON for rest_framework)

from rest_framework import serializers

from .models import Content, Video, Step

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'content_type', 'category', 'normal_type', 'title_video', 'author']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'isTitle', 'content', 'url', 'title', 'thumbnail']


class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'content', 'step_number', 'title', 'description', 'video']
