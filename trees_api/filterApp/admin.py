from django.contrib import admin

# Register your models here.
from .models import SimpleFilter, FilterRef

# Admin Models
class SimpleFilterAdmin(admin.ModelAdmin):
    list_display = ('id', 'questionRef', 'answerValue', 'effect', 'effectStrength')
    list_filter = ('questionRef', 'answerValue', 'effect', 'effectStrength')
    search_fields = ('questionRef', 'answerValue', 'effect', 'effectStrength')
    ordering = ['questionRef']

class FilterRefAdmin(admin.ModelAdmin):
    list_display = ('id', 'userRef', 'simpleFilterRef', 'date', 'time')
    list_filter = ('userRef', 'simpleFilterRef', 'date', 'time')
    search_fields = ('userRef', 'simpleFilterRef', 'date', 'time')
    ordering = ['userRef']

# Register your models here.
admin.site.register(SimpleFilter, SimpleFilterAdmin)
admin.site.register(FilterRef, FilterRefAdmin)