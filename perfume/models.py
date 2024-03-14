# Create your models here.
from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.
# Models are saved in the database
# Think of a model in the database as a spreadsheet with columns (fields) and rows (data)
class Designer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.URLField(max_length=300)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Note(models.Model):
    note = models.CharField(max_length=200)
    image = models.URLField(max_length=300)

    class Meta:
        ordering = ["note"]

    def __str__(self) -> str:
        return self.note


class Accord(models.Model):
    accord = models.CharField(max_length=200)

    class Meta:
        ordering = ["accord"]

    def __str__(self) -> str:
        return self.accord


class Perfume(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=300)

    # a designer can have many perfumes, but perfume can only have 1 designer
    designer = models.ForeignKey(Designer, on_delete=models.RESTRICT)

    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the perfume"
    )
    tags = TaggableManager()

    notes = models.ManyToManyField(Note)
    accords = models.ManyToManyField(Accord)
    rating = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.name} by {self.designer}"
