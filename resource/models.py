from django.db import models


class Category(models.Model):
    active = models.BooleanField(default=True)

    name = models.CharField(max_length=128)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order',)
        verbose_name_plural = "categories"


class Resource(models.Model):
    active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "resources"
