from django.db import models


class Tweet(models.Model):
    content   = models.CharField(max_length=256)
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
