from django.db import models

from questionApp.models import Question, DemoQuestion
from userApp.models import User, Answer, CurrentAnswer

# Create your models here.

class SimpleFilter(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    questionRef = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerValue = models.IntegerField() # [0, 11]
    effect = models.IntegerField() # [0, 1]
    # effect legend:
    # 0 -> decrease likelihood of recommendation
    # 1 -> increase likelihood of recommendation

    # optional fields



class FilterRef(models.Model):
    # required fields
    userRef = models.ForeignKey(User, on_delete=models.CASCADE)
    simpleFilterRef = models.ForeignKey(SimpleFilter, on_delete=models.CASCADE)

    # optional fields
    date = models.DateTimeField(auto_now_add=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)
