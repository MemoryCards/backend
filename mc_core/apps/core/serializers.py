from rest_framework import serializers
from .models import Card, Deck
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'question', 'answer', ]


class DeckSerializer(serializers.ModelSerializer):
    cards = Card.objects.filter(pk=1)

    class Meta:
        model = Deck
        fields = ['id', 'name', 'description', 'cards']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']