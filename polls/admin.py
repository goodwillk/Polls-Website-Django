from django.contrib import admin
from .models import *

# admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(SuggestQuestion)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ("What's inside the question",  {"fields": ['question_text']}),
    #     ("Date Information",            {"fields": ['pub_date']}),
    #     ("was_published_recently",      {"fields": ['was_published_recently']})
    # ]
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)