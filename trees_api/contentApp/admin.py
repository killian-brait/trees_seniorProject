from django.contrib import admin

from .models import Content, Step, Video

# Register your models here.
admin.site.register(Content)
admin.site.register(Step)
admin.site.register(Video)