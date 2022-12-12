from django.db import models


class Card(models.Model):
    title = models.CharField()
    decf = models.ForeignKey()
