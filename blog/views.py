from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import Post
from siteapp.views import MultiSerializerViewSetMixin
from .serializers import PostListSerializer, PostSerializer


class PostViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializers = {
        'list': PostListSerializer
    }
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['created']
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.all()

        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = self.queryset.filter(tags__slug=tag)
        return queryset
