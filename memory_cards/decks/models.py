from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=255, unique=True)
    depiction = models.TextField(max_length=2000)
    categories = models.ForeignKey('cards.Category', on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return f"{self.name}"
