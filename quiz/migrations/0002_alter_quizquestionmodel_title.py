# Generated by Django 4.1.2 on 2022-10-10 05:40

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestionmodel',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]
