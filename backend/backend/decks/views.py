from .models import Deck
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import DeckSerializer


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
