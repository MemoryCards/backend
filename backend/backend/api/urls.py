from django.urls import include, path
from rest_framework import routers
from .views import CardViewSet,DeckViewSet, CategoryViewSet
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'decks', DeckViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]