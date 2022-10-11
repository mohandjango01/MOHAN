from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save

from onlineexam_core.utils import slug_pre_save_receiver

User = get_user_model()

# Create your models here.
class studentStudentModel(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name="studentStudentModel_user")
    age=models.IntegerField()
    city=models.CharField(max_length=100)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.student)


pre_save.connect(slug_pre_save_receiver, sender=studentStudentModel)