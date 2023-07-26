from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm, TaskUpdateForm

from todo_list_app.models import Task, Tag


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "task/task_list.html"
    paginate_by = 5


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag/tag_list.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tag/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tag/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


def toggle_task_status(request, pk: int) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)

    if task.is_done:
        task.is_done = False
        task.save()
    else:
        task.is_done = True
        task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")