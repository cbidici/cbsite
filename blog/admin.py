from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('site', 'tags', 'owner', 'slug', 'title', 'summary', 'text')
    list_display = ('title', 'owner', 'updated')
    search_fields = ('title',)
    readonly_fields = ('slug',)


admin.site.register(Post, PostAdmin)
