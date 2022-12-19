from rest_framework import serializers

from .models import Deck, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class DeckSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Deck
        fields = ['name', 'description', 'category']
