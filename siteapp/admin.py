from django.contrib import admin

from .models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ('sub_domain', 'name', 'title', 'updated')


admin.site.register(Site, SiteAdmin)
