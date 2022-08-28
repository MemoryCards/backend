from django.db import models

#from main.models import Timestamped

from main.models import Tags, Categories



class Card(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField(max_length=2000)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

'''
class UserCreatedCard(Card, Timestamped):
    usser = models.OneToOneRel()
'''
