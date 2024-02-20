from django.contrib import admin
from .models import Question, Answer, Category, QuizHistory, Sets

# Register your models here.
admin.site.register(Category)


class AnswerAdmin(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(QuizHistory)
admin.site.register(Sets)
