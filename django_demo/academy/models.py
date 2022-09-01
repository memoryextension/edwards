from django.db import models

from django_demo.academy.utils import get_random_word


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(to = Classroom, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)