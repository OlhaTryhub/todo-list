from django.urls import path

from .views import (TaskListView,
                    TagListView,
                    TaskCreateView,
                    TagCreateView,
                    TagUpdateView,
                    TagDeleteView,
                    TaskUpdateView,
                    TaskDeleteView,
                    toggle_task_status)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("<int:pk>/toggle-satus/", toggle_task_status, name="toggle-task-satus")
]

app_name = "todo"
