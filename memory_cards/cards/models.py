from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=2000)
    deck_id = models.ForeignKey('decks.Deck', on_delete=models.SET_NULL, null=True )
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.question}"


'''
class UserCard(Card, Timestamped):
    card_id = models.ForeignKey(Card)
    question = models.CharField(max_length=255, unique=True)
    response = models.TextField(max_length=2000, unique=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    author = models.OneToOneRel()
    votes = models.ForeignKey(Votes, on_delete=models.CASCADE)


class Votes(models.Model):
    user_card_id = models
    count = models.IntegerField()
    class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

'''

