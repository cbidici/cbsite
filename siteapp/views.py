from rest_framework.viewsets import ModelViewSet

from .filters import SiteFilterBackend


class SiteModelViewSet(ModelViewSet):

    def filter_queryset(self, queryset):
        queryset = super(SiteModelViewSet, self).filter_queryset(queryset)
        return SiteFilterBackend().filter_queryset(self.request, queryset, self)
