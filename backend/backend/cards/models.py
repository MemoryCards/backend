from django.db import models
from decks.models import Deck


class Card(models.Model):
    title = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='deck')
