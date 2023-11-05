from django.contrib import admin
from .models import Quiz, IncorrectAnswer, Category, Difficulty, Type


class IncorrectAnswerInline(admin.TabularInline):
    model = IncorrectAnswer


class QuizAdmin(admin.ModelAdmin):
    inlines = [IncorrectAnswerInline]


admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Type)
admin.site.register(Quiz, QuizAdmin)
