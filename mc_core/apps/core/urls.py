from django.urls import include, path
from rest_framework import routers
# from .views import UserViewSet, GroupViewSet
from .views import CardViewSet, DeckViewSet, UserViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'decks', DeckViewSet)
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
