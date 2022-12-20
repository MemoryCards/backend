from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=256)


class Deck(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(max_length=250)
    category = models.ManyToManyField(Category, related_name='category')


class Card(models.Model):
    title = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='deck')
