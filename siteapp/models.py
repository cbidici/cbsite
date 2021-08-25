from django.db import models


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    sub_domain = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SiteModel(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Tag(SiteModel, models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128, unique=True)
    tag = models.CharField(max_length=128)

    def __str__(self):
        return self.tag


class TagsModel(models.Model):
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True
