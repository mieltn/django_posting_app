import datetime

from django.db import models
from django.utils import timezone

class Idea(models.Model):
    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    post_title = models.CharField(max_length=200)
    post_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)


class Comment(models.Model):
    def __str__(self):
        return self.comment_text

    post = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)
