from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=3000)


class Label(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    title = models.CharField(max_length=3000)
    is_done = models.BooleanField(default=False)
    labels = models.ManyToManyField(Label)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.PROTECT)

    due_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
