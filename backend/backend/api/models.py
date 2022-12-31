from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)


class Deck(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(max_length=250, default="")
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return str(self.name)


class Card(models.Model):
    title = models.CharField(max_length=50)
    question = models.TextField(default='')
    answer = models.TextField(default='')
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return str(self.title)
