from django.db import models


class TodoTask(models.Model):
    title = models.CharField(max_length=121)
    active = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    owner = models.CharField(max_length=121)
    create_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
