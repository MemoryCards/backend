from django.db import models



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



