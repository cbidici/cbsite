from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=512)
    text=models.TextField()
    owner=models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
