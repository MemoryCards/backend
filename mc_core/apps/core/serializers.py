from rest_framework import serializers
from .models import Card, Deck
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'question', 'answer', 'deck']


class ShortCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['question']


class DeckSerializer(serializers.ModelSerializer):
    cards = ShortCardSerializer(many=True)

    class Meta:
        model = Deck
        fields = ['id', 'name', 'description', 'created_by', 'cards']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']
