from django.contrib import admin
from .models import User, Answer, CurrentAnswer

# Admin Models
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'phone_number', 'bio')
    list_filter = ('username', 'email', 'password', 'phone_number', 'bio')
    search_fields = ('username', 'email', 'password', 'phone_number', 'bio')
    ordering = ['username']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'slide_val', 'date', 'time')
    list_filter = ('slide_val', 'date', 'time')
    search_fields = ('slide_val', 'date', 'time')

class CurrentAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'answerId', 'questionId')
    list_filter = ('userId', 'answerId', 'questionId')
    search_fields = ('userId', 'answerId', 'questionId')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(CurrentAnswer, CurrentAnswerAdmin)