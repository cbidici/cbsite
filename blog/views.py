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
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            queryset = self.queryset.filter(owner__username=owner)

        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = self.queryset.filter(tags__slug=tag)
        return queryset
