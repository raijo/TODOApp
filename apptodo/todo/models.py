from django.db import models


class Todo(models.Model):
    todo_title = models.CharField(max_length=64, blank=True, null=True)
    todo_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.todo_title, self.todo_content)
