from rest_framework import serializers

from .models import Post
from siteapp.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['url', 'id', 'owner', 'title', 'summary', 'text', 'created', 'tags']


class PostListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['url', 'id', 'owner', 'title', 'summary', 'created']
        read_only_fields = ['url', 'id', 'owner', 'title', 'summary', 'created']
