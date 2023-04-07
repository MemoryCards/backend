from django.db import models
from .abstract_models import BaseCardModel, TimestampModel, NameSlugModel




class Category(NameSlugModel, TimestampModel):
    description = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)


class Deck(NameSlugModel):
    description = models.TextField(max_length=250, default="")
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return str(self.name)


class Card(NameSlugModel, BaseCardModel):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return str(self.title)
