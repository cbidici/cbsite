from django.urls import path, include
from rest_framework import routers

from .views import TagViewSet

router = routers.SimpleRouter()
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
