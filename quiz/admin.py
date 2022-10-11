from django.contrib import admin

from quiz.models import quizQuestionModel, quizChoiceModel

# Register your models here.
admin.site.register(quizQuestionModel)
admin.site.register(quizChoiceModel)
