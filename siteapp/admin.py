from django.contrib import admin

from .models import Site, Tag


class SiteAdmin(admin.ModelAdmin):
    list_display = ('sub_domain', 'name', 'title', 'updated')


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Site, SiteAdmin)
admin.site.register(Tag, TagAdmin)
