from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from todo_list_app.models import Task, Tag


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "task/task_list.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag/tag_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")