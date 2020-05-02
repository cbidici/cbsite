from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = (('Meta', {
        'fields': ('title', 'owner',)
    }), ('Post', {
        'classes': ('short',), 'fields': ('text',),
    }),)


admin.site.register(Post)
