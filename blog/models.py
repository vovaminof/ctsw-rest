from ckeditor.fields import RichTextField
from datetime import datetime
from taggit.managers import TaggableManager

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)
    about = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=datetime.now)

    title = models.CharField(max_length=128)
    text = RichTextField()
    image = models.ImageField()
    published = models.BooleanField(default=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title
