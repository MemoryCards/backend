from .models import Card, Deck, Category
from rest_framework import viewsets, filters
from .serializers import CardsSerializer, DeckSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def destroy(self, request, *args, **kwargs):
        deck = self.get_object()
        deck.delete()
        return Response('Deck has been removed')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response('Category has been removed')

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardsSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['title']


    @action(detail=False)
    def list_by_deck(self, request, *args, **kwargs):
        pass


    def update(self, request, *args, **kwargs):
        card = self.get_object()
        card.title = request.data['title']
        card.question = request.data['question']
        card.answer = request.data['answer']
        card.deck = request.data['deck']
        card.save()

        serializer = CardsSerializer(card, many=False)
        return Response(serializer.data)



    def destroy(self, request, *args, **kwargs):
        card = self.get_object()
        card.delete()
        return Response('Card has been removed')
