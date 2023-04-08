from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CardSerializer, DeckSerializer, CategorySerializer
from .models import Card, Deck, Category
from .serializers import UserSerializer
from django.contrib.auth.models import User


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # permission_classes = [IsAuthenticated]


class DeckViewSet(ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
