from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .models import Post
from .permissions import IsOwnerOrReadOnlyObject
from .serializers import PostListSerializer, PostSerializer


class MultiSerializerViewSetMixin:
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)


class PostViewSet(MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializers = {
        'list': PostListSerializer
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
