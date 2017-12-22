from django.db import models


class Tweet(models.Model):
    content = models.TextField()

    def __srt__(self):
        return str(self.content)
