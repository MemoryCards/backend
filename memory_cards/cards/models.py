from django.db import models


class Card(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField(max_length=2000)
    # tags
    # categories
