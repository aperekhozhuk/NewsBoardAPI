from django.db import models
from django.contrib.auth.models import User
import datetime
from . import settings


class Post(models.Model):
    title = models.CharField(max_length=settings.TITLE_MAX_LENGTH)
    link = models.CharField(max_length=settings.LINK_MAX_LENGTH)
    creation_date = models.DateField(default=datetime.date.today)
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=settings.AUTHOR_NAME_MAX_LENGTH)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author_name = models.CharField(max_length=settings.AUTHOR_NAME_MAX_LENGTH)
    content = models.TextField()
    creation_date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
