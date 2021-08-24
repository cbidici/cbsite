from django.db import models
from markdownme.fields import MarkdownField
from siteapp.models import SiteModel, TagsModel


class Post(SiteModel, TagsModel, models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512)
    summary = MarkdownField(max_length=500, rows=10)
    text = MarkdownField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
