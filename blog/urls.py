from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('blog/', include(router.urls))
]
