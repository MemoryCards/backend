from .models import Card
from rest_framework import serializers

#from ..decks.serializers import DeckSerializer


class CardSerializer(serializers.HyperlinkedModelSerializer):
    #deck = DeckSerializer(many=False)

    class Meta:
        model = Card
        fields = ['title', 'question','answer','deck']