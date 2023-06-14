from django.shortcuts import render

from rest_framework import viewsets

from .serializers import QuestionSerializer, DemoQuestionSerializer
from .models import Question, DemoQuestion

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

class DemoQuestionViewSet(viewsets.ModelViewSet):
    queryset = DemoQuestion.objects.all().order_by('id')
    serializer_class = DemoQuestionSerializer