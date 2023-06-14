from django.db import models

# Import Trees questionApp models
from questionApp.models import Question, DemoQuestion

# User model
# This model stores user information used for login/authentication and structuring the user profile page
# TO-DO: 
#  [ ] Build the user model out to include personality data and demographic/group data fields
class User(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    # optional fields
    phone_number = models.CharField(max_length=100, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bio = models.TextField(blank=True)


    def __str__(self):
        ret_string = "Username: " + self.username + " Email: " + self.email
        return ret_string
    

# Answer model
# This model stores the answers to the slider questions 
class Answer(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    # [0, 11]
    #  -> 11 is "YesYesYesYesYes"
    #  -> 5 is "Indifferent"
    #  -> 0 is "NoNoNoNoNo"
    slide_val = models.IntegerField()

    # optional fields
    date = models.DateTimeField(auto_now_add=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        ret_string = "Answer: " + str(self.slide_val)
        return ret_string



# Current Answer model
# This model links the User and Answer models together to store the user's
# current answers to the slider questions in a many-to-many relationship between
# the User and Answer models
class CurrentAnswer(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    answerId = models.ForeignKey(Answer, on_delete=models.CASCADE, default=-1)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        ret_string = "User: " + self.userId.username + " Answer: " + str(self.answerId.slide_val)
        return ret_string
    
class PastAnswer(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    answerId = models.ForeignKey(Answer, on_delete=models.CASCADE, default=-1)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        ret_string = "User: " + self.userId.username + " Answer: " + str(self.answerId.slide_val)
        return ret_string



    

    