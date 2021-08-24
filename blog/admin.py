from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'updated')
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
