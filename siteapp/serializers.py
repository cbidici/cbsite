from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['slug', 'tag']


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['slug', 'tag']
        read_only_fields = ['slug', 'tag']