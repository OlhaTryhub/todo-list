from django.shortcuts import render
from django.views import generic

from todo_list_app.models import Task, Tag


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "task/task_list.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag/tag_list.html"
