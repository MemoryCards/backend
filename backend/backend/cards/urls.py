from django.urls import include, path
from rest_framework import routers
from .views import CardViewSet

router = routers.DefaultRouter()
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('', include(router.urls))
]
