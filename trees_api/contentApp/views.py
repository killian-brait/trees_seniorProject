from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ContentSerializer, VideoSerializer, StepSerializer
from .models import Content, Video, Step

# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('id')
    serializer_class = ContentSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all().order_by('id')
    serializer_class = StepSerializer
