# serializers.py 
# Purpose: Serializers for the User App (turn models into JSON for rest_framework)

from rest_framework import serializers

# FilterRef isn't available to the REST API because it's used for backend
# filtering
from .models import SimpleFilter

class SimpleFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimpleFilter
        fields = ['id', 'questionRef', 'answerValue', 'effect', 'effectStrength']
