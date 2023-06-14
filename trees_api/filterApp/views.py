from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import SimpleFilterSerializer
from .models import SimpleFilter

# Create your views here.

class SimpleFilterViewSet(viewsets.ModelViewSet):
    queryset = SimpleFilter.objects.all().order_by('id')
    serializer_class = SimpleFilterSerializer