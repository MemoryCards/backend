from django.db import models
from django.template.defaultfilters import slugify


class TimestampModel(models.Model):
    """Abstract base class for models with created_at and updated_at fields."""
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class BaseCardModel(models.Model):
    """Abstract base class for cards models, with title, question and answer"""

    question = models.TextField(default='')
    answer = models.TextField(default='')

    class Meta:
        abstract = True


class NameSlugModel(models.Model):
    """Abstract base class for models with name and slug fields."""
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
