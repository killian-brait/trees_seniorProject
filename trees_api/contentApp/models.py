from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class Content(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    # normalized fields
    normal_type = models.IntegerField() # 0 for video, 1 for step

    # optional fields
    title_video = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'content_type'], name='unique_content')
        ]
    

class Video(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    isTitle = models.BooleanField() # True if the video is the title video, False otherwise
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)

    # optional fields
    thumbnail = models.CharField(max_length=100, blank=True)


class Step(models.Model):
    # trees_internal id
    id = models.AutoField(primary_key=True)

    # required fields
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    step_number = models.IntegerField()

    # optional fields
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)