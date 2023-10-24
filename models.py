from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_quill.fields import QuillField


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = QuillField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:list')

    def __str__(self):
        return self.title