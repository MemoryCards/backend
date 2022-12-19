from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=256)


class Deck(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(max_length=250)
    category = models.ManyToManyField(Category, related_name='category')
