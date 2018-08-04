from ckeditor.fields import RichTextField
from django.db import models


class About(models.Model):
    active = models.BooleanField(default=True)

    name = models.CharField(max_length=128)
    summary = models.CharField(max_length=256, blank=True, null=True)
    content = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "about"
