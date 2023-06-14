# serializers.py 
# Purpose: Serializers for the User App (turn models into JSON for rest_framework)

from rest_framework import serializers

from .models import User, Answer, CurrentAnswer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'bio']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'slide_val', 'date', 'time']


# User-Answer Serializer that uses the CurrentAnswer model to join together
# the User and Answer returning the username, slide_val, date, and time
# -- 
# class UserAnswerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CurrentAnswer
#         fields = ['userId', 'questionId', 'slide_val', 'date', 'time']