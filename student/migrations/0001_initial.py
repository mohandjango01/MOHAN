# Generated by Django 4.1.2 on 2022-10-10 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='studentStudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentStudentModel_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
