from django.contrib import admin

from.models import Question, Answer, Vote

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Vote)


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}
    #    'classes': ['coll']
    ]

admin.site.register(Question, QuestionAdmin)
