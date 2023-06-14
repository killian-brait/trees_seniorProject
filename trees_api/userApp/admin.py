from django.contrib import admin
from .models import User, Answer, CurrentAnswer

# Register your models here.
admin.site.register(User)
admin.site.register(Answer)
admin.site.register(CurrentAnswer)