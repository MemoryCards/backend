from django.db import models
# from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   null=True)

    def __str__(self):

        return self.question[:55]


class Deck(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    cards = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='cards'
    )

    def __str__(self):
        return self.name
