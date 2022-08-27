from django.db import models

from main.models import Timestamped

#from tags.moodel import Tag



class Card(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField(max_length=2000)
    # tags


'''
class UserCreatedCard(Card, Timestamped):

    usser = models.OneToOneRel()
    starus
    vouts
    coments
'''
