from django.db import models
from django.urls import reverse
import django.utils.timezone
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)

    def __str__(self):
        return self.title

   
