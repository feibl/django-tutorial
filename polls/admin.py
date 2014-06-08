from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    # First: Title, Second: Fields
    fieldsets = [
        (
            None,
            {'fields': ['question_text']}
        ),
        (
            'Date information',
            {'fields': ['pub_date'], 'classes': ['collapse']}
        ),
    ]

admin.site.register(Question, QuestionAdmin)
