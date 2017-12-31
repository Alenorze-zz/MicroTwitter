from django.db import models
from django.urls import reverse_lazy

from tweets.models import Tweet


class HashTag(models.Model):
    tag = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
