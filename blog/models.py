from django.db import models


class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
