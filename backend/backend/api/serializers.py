from rest_framework import serializers
from .models import Deck, Category, Card


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class DeckSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Deck
        fields = ('name', 'description', 'category')


class CardsSerializer(serializers.ModelSerializer):
    deck = DeckSerializer(many=False)

    class Meta:
        model = Card
        fields = ('title', 'question', 'answer', 'deck')
