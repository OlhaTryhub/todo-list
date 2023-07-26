from django.urls import path

from .views import (TaskListView,
                    TagListView,
                    TaskCreateView,
                    TagCreateView,
                    TagUpdateView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "todo"
