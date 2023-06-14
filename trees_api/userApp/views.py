# from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserSerializer, AnswerSerializer
from .models import User, Answer

# Create your views here.

# UerViewSet handles GET, POST
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

# AnswerViewSet handles GET, POST
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('id')
    serializer_class = AnswerSerializer