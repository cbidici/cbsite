from rest_framework.viewsets import ModelViewSet
from .models import Tag
from .serializers import TagListSerializer, TagSerializer


class MultiSerializerViewSetMixin:
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)


class TagViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    serializers = {
        'list': TagListSerializer
    }
