from mc_core.apps.core.models.models import (
    Card,
    Category,
    Deck
)
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['name', ]