from django.urls import include, path
from rest_framework import routers
from .views import DeckViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'decks', DeckViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]