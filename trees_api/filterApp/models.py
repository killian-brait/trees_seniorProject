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
    effect = models.IntegerField(default=0) # [0, 1]
    effectStrength = models.IntegerField(default=0) # [0, 10]
    # effect legend:
    # 0 -> decrease likelihood of recommendation
    # 1 -> increase likelihood of recommendation

    # optional fields

    def __str__(self):
        effect_string = ""
        if self.effect == 0:
            effect_string = "\ndecrease recommendation likelihood"
        elif self.effect == 1:
            effect_string = "\nincrease recommendation likelihood"

        ret_string = "Strength: " + str(self.effectStrength) + effect_string + " ------- Question: " + self.questionRef.question + ", Answer: " + str(self.answerValue)

        # ret_string = "Question: " + self.questionRef.question + ", Answer: " + str(self.answerValue) + ", Effect: " + effect_string
        return ret_string



class FilterRef(models.Model):
    # required fields
    userRef = models.ForeignKey(User, on_delete=models.CASCADE)
    simpleFilterRef = models.ForeignKey(SimpleFilter, on_delete=models.CASCADE)

    # optional fields
    date = models.DateTimeField(auto_now_add=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        ret_string = "User: " + self.userRef.username + ", Filter: " + str(self.simpleFilterRef)
        return ret_string
