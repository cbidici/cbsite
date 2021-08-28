from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('tags', 'slug', 'title', 'summary', 'text')
    list_display = ('title', 'updated')
    search_fields = ('title',)
    readonly_fields = ('slug',)


admin.site.register(Post, PostAdmin)
