from django.db import models


class TodoList(models.Model):
    """A collection of tasks."""

    name = models.CharField(max_length=255)
    todos = models.JSONField(default=list)

    def add_todo(self, todo: str) -> None:
        self.todos.append(todo)
        self.save()
