from ckeditor.fields import RichTextField
from django.db import models


class Ministry(models.Model):
    active = models.BooleanField(default=True)

    name = models.CharField(max_length=128)
    content = RichTextField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ministries"
