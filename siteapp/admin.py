from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    fields = ('slug', 'tag')
    list_display = ('slug', 'tag')
    readonly_fields = ('slug',)


admin.site.register(Tag, TagAdmin)
