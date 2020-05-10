from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from siteapp.views import SiteModelViewSet

from .models import Post
from .permissions import IsOwnerOrReadOnlyObject
from .serializers import PostListSerializer, PostSerializer


class MultiSerializerViewSetMixin:
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)


class PostViewSet(MultiSerializerViewSetMixin, SiteModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializers = {
        'list': PostListSerializer
    }
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['created']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
