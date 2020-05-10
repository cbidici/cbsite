from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=64)
    sub_domain = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SiteModel(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        abstract = True
