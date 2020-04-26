from django.db import models
from markdownme.fields import MarkdownField


class Post(models.Model):
    title=models.CharField(max_length=512)
    text=MarkdownField()
    owner=models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
