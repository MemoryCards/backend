from .models import Card
from rest_framework import viewsets, permissions
from .serializers import CardSerializer
from rest_framework.response import Response

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CardSerializer(queryset, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        card = self.get_object()
        card.delete()
        return Response('Card has been removed')
