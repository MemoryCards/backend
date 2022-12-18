from .models import Deck, Category
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import DeckSerializer, CategorySerializer


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer