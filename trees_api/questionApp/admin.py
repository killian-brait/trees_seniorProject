from django.contrib import admin
from .models import Question, DemoQuestion

# Admin Models
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'reversed', 'isNormal', 'num_vals', 'question', 'more_info')
    list_filter = ('reversed', 'isNormal', 'num_vals', 'question')
    search_fields = ('reversed', 'isNormal', 'num_vals', 'question')
    ordering = ['id']

class DemoQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'options', 'more_info', 'demo_type')
    list_filter = ('question', 'options', 'demo_type')
    search_fields = ('question', 'options', 'demo_type')
    ordering = ['id']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(DemoQuestion, DemoQuestionAdmin)