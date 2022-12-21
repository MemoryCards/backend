from rest_framework import serializers
from .models import Deck, Category, Card


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('title', 'question', 'answer')


class DeckSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    cards = CardsSerializer(many=True)
    class Meta:
        model = Deck
        fields = ('name', 'description', 'category', 'cards')
