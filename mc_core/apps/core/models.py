from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class NameSlugModel(models.Model):
    """Abstract base class for models with name and slug fields."""
    name = models.CharField(max_length=255, unique=True, default='')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(NameSlugModel):
    pass


class Deck(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return self.name


class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='cards'
    )

    def __str__(self):
        return self.question[:50]
