from django.contrib import admin

# Register your models here.
from .models import SimpleFilter

# Admin Models
class SimpleFilterAdmin(admin.ModelAdmin):
    list_display = ('id', 'questionRef', 'answerValue', 'effect', 'effectStrength')
    list_filter = ('questionRef', 'answerValue', 'effect', 'effectStrength')
    search_fields = ('questionRef', 'answerValue', 'effect', 'effectStrength')
    ordering = ['questionRef']

# Register your models here.
admin.site.register(SimpleFilter, SimpleFilterAdmin)