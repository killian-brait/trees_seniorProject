from django.contrib import admin

from .models import Content, Step, Video

# Admin Models
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'score', 'content_type', 'category', 'normal_type')
    ordering = ['id']

class StepAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'step_number', 'title', 'description', 'video')
    ordering = ['id']

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'isTitle', 'content', 'url', 'thumbnail')
    ordering = ['id']


# Register your models here.
admin.site.register(Content, ContentAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Video, VideoAdmin)