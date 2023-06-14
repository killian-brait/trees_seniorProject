from django.contrib import admin
from .models import Question, DemoQuestion

# Register your models here.
admin.site.register(Question)
admin.site.register(DemoQuestion)