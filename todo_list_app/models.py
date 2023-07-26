from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(to=Tag)
