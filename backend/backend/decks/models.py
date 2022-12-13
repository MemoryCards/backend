from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=256)


class Deck(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=256)
    category_id = models.ForeignKey(Category.pk())
