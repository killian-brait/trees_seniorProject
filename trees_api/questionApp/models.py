from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# Question model
# This model stores the questions that are displayed on the slider page
# -> since slider-answers will be hardcoded with numbers, the database won't contain any information to create
#    the questions with custom text on the top and the bottom of the slider - instead 
class Question(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # machine learning/GPT fields
    isBig5 = models.BooleanField(default=False) # True if this is a big5 personality question
    big5cat = models.CharField(max_length=100, default="") # Only set if isBig5 is true, otherwise "n/a" or missing_val

    # required fields
    reversed = models.BooleanField() # True if the slider is reversed, False if the slider is normal
    isNormal = models.BooleanField() # True if slider has 11 values, False otherwise
    num_vals = models.IntegerField() # number of values on the slider [1, 11]
    question = models.CharField(max_length=100) # question text

    # optional fields
    more_info = models.TextField(blank=True)
    # question_image = models.ImageField(upload_to='question_images/', blank=True)

    def __str__(self):
        ret_string = "Question: " + self.question + " Number of Value: " + str(self.num_vals)
        return ret_string
    
    def clean(self):
        # Perform data validation for the entire Question model
        # -> this function is called automatically when the model is saved
        if self.num_vals < 1 or self.num_vals > 11:
            raise ValidationError('num_vals must be between 1 and 11')
        

# Demographic question model
# This model stores the demographic questions that have distinct options and are
# always multiple choice with at least 2 options
class DemoQuestion(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    question = models.CharField(max_length=100) # question text
    options = models.TextField() # comma-separated list of options

    # optional fields
    more_info = models.TextField(blank=True)
    demo_type = models.CharField(max_length=100, blank=True) # type of demographic question
    # question_image = models.ImageField(upload_to='question_images/', blank=True)

    def __str__(self):
        ret_string = "Question: " + self.question + " Options: " + self.options
        return ret_string
    
    def clean(self):
        # Perform data validation for the entire DemoQuestion model
        # -> this function is called automatically when the model is saved

        # check if the TextField is actually a comma-separated list
        if len(self.options.split(',')) == 1:
            raise ValidationError('options must be a comma-separated list')

        if len(self.options.split(',')) < 2:
            raise ValidationError('options must have at least 2 options')
        
        