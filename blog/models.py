from django.db import models
from markdownme.fields import MarkdownField
from siteapp.models import TagsModel
from slugify import slugify


class Post(TagsModel, models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=512, unique=True)
    title = models.CharField(max_length=512)
    summary = MarkdownField(max_length=500, rows=10)
    text = MarkdownField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.title)
        super(Post, self).save(force_insert, force_update)

    def __str__(self):
        return self.title
