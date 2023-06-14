# serializers.py 
# Purpose: Serializers for the User App (turn models into JSON for rest_framework)

from rest_framework import serializers

from .models import Question, DemoQuestion

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'reversed', 'isNormal', 'num_vals', 'question', 'more_info']

class DemoQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DemoQuestion
        fields = ['id', 'question', 'options', 'more_info', 'demo_type']