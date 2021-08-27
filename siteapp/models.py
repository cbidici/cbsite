from django.db import models
from slugify import slugify


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=128, unique=True)
    tag = models.CharField(max_length=128)

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.tag)
        super(Tag, self).save(force_insert, force_update)

    def __str__(self):
        return self.tag


class TagsModel(models.Model):
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True
