from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from rest_framework import serializers

from onlineexam_core.utils import slug_pre_save_receiver

User = get_user_model()
"""
question

title = required

slug = required
date_created = required 

1 hr create multiple questions so fk.
"""
# def function(value):
#     if value:
#         raise serializers.ValidationError("erorr")

# Create your models here.
# <editor-fold desc="QUESTION">
class quizQuestionModel(models.Model):
    title = models.TextField(unique=True)
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizQuestionModel_user")
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_question_by_choices(self):
        return self.quizChoiceModel_question.text


pre_save.connect(slug_pre_save_receiver, sender=quizQuestionModel)
# </editor-fold>

"""
choice

question = required
text = required

slug = required
date_created = required 

"""




# <editor-fold desc="CHOICES">
class quizChoiceModel(models.Model):
    question = models.ForeignKey(quizQuestionModel, on_delete=models.CASCADE, related_name="quizChoiceModel_question")
    text = models.TextField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.text)


pre_save.connect(slug_pre_save_receiver, sender=quizChoiceModel)
# </editor-fold>
