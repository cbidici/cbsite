from rest_framework import serializers

from .models import Post
from siteapp.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='post-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = ['url', 'id', 'slug', 'title', 'summary', 'text', 'created', 'tags']


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = ['url', 'id', 'slug', 'title', 'summary', 'created']
        read_only_fields = ['url', 'id', 'slug', 'title', 'summary', 'created']
